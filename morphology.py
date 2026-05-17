import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_opening
from scipy.ndimage import binary_fill_holes
from skimage.measure import label
import hardware.buzzer as buzzer

def create_binary_mask(image_path):
    print("🔍 [Vision] Step 2: Creating Binary Mask (Custom Flex Filter)...")
    img = cv2.imread(image_path)
    if img is None: return None

    # 1. חיתוך ROI (חייב להיות זהה לשלבים הקודמים)
    # -------------------------------------------
    H, W = img.shape[:2]
    roi_w = max(1, W // 5)
    roi_h = max(1, H // 5)
    x_start = (W - roi_w) // 2
    y_start = (H - roi_h) // 2
    
    # שומרים גם צבע (לזיהוי פלקס) וגם אפור (ליצירת מסכה ראשית)
    roi_color = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

    # 2. יצירת מסכה ראשונית (לפי בהירות/כהות של הרכיב)
    # -------------------------------------------
    DARK_THRESHOLD = 35 #35
    _, dark_mask = cv2.threshold(roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

    # 3. ניקוי ה-FLEX לפי ערכי HSV שנתת
    # -------------------------------------------
    hsv = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)

    # --- טווח 1: ירוק כהה (החלק הירוק בפלקס) ---
    # H: 87-96, S: 101-193, V: 38-60
    lower_green = np.array([87, 101, 38])
    upper_green = np.array([96, 193, 60])
    mask_flex_green = cv2.inRange(hsv, lower_green, upper_green)

    # --- טווח 2: נחושת (החלק החום/כתום בפלקס) ---
    # H: 15-37, S: 65-120, V: 30-80
    # הערה: זה בטוח כי ה-Value מקסימום 80, בעוד ששבר צהוב מתחיל מ-90
    #lower_copper = np.array([15, 30, 30]) #שיניתי טווח
   # upper_copper = np.array([80, 120, 80]) #שיניתי טווח
    #mask_flex_copper = cv2.inRange(hsv, lower_copper, upper_copper)

    # איחוד שני המסכות של הפלקס (ירוק או נחושת)
    #flex_mask_total = cv2.bitwise_or(mask_flex_green, mask_flex_copper)

    # הרחבה קלה (Dilate) כדי לכסות את קצוות הפלקס שלא נתפסו בול
    kernel_flex = np.ones((5, 5), np.uint8)
    flex_mask_total = cv2.dilate(mask_flex_green, kernel_flex, iterations=1)
    #flex_mask_total = cv2.dilate(flex_mask_total, kernel_flex, iterations=2)

    # === ביצוע המחיקה ===
    # כל פיקסל שזוהה כפלקס - נמחק מהמסכה הראשית (הופך לשחור)
    dark_mask[flex_mask_total > 0] = 0

    # 4. חיתוך גיאומטרי נוסף לביטחון (צד ימין)
    # -------------------------------------------
    # אנחנו עדיין מוחקים את ה-15% הימניים ביותר למקרה שמשהו התפספס בצבע
    h_mask, w_mask = dark_mask.shape
    cutoff_x = int(w_mask * 0.85)
    dark_mask[:, cutoff_x:] = 0

    # 5. ניקוי מורפולוגי רגיל (סגירת חורים)
    # # -------------------------------------------
    # kernel = np.ones((3, 3), np.uint8)
    # mask_cleaned = cv2.morphologyEx(dark_mask, cv2.MORPH_OPEN, kernel)
    # mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)
    
    # --- מעבר ראשון: עדין (3x3) ---
    # מנקה נקודות קטנות ("אבק")
    kernel_small = np.ones((5, 5), np.uint8)
    mask_pass1 = cv2.morphologyEx(dark_mask, cv2.MORPH_OPEN, kernel_small)
    mask_pass1 = cv2.morphologyEx(mask_pass1, cv2.MORPH_CLOSE, kernel_small)

    # --- מעבר שני: קצת יותר גדול (5x5) ---
    # מחליק קצוות וסוגר חורים בינוניים
    kernel_large = np.ones((5, 5), np.uint8)
    #kernel_larger = np.ones((7, 7), np.uint8)
    mask_pass2 = cv2.morphologyEx(mask_pass1, cv2.MORPH_OPEN, kernel_small)
    mask_final = cv2.morphologyEx(mask_pass2, cv2.MORPH_CLOSE, kernel_large)

    
    
    # שמירה
    dir_name = os.path.dirname(image_path)
    base_name = os.path.basename(image_path)
    name_no_ext = os.path.splitext(base_name)[0]
    
    mask_path = os.path.join(dir_name, f"{name_no_ext}_MASK.PNG")
    cv2.imwrite(mask_path, mask_final)
    
    # שורה לדיבאג: אם תרצי לראות מה המחשב זיהה כ"פלקס", תורידי את ההערה:
    # cv2.imwrite(os.path.join(dir_name, f"{name_no_ext}_DEBUG_FLEX.PNG"), flex_mask_total)

    print(f" Saved Mask (Flex Removed): {mask_path}")
    return mask_path


def check_skeleton_continuity(mask_path):
    # --- אין שינוי בפונקציה הזו ---
    print("🔍 [Vision] Step 3: Checking Skeleton Continuity...")
    if not mask_path or not os.path.exists(mask_path): return False

    img = cv2.imread(mask_path, 0)
    bw = img > 127
    if np.mean(bw) > 0.5: bw = ~bw

    bw = remove_small_objects(bw, min_size=500)
    se = disk(6)
    bw = binary_closing(bw, se)
    bw = binary_opening(bw, se)
    bw = binary_fill_holes(bw)
    skel = skeletonize(bw)
    
    for _ in range(15):
        endpoints = _find_endpoints(skel)
        skel[endpoints] = False

    h, w = bw.shape
    roi_frac = 0.50
    roi_w = int(w * roi_frac)
    roi_h = int(h * roi_frac)
    x1 = (w - roi_w) // 2
    y1 = (h - roi_h) // 2
    
    roi_mask = np.zeros((h, w), dtype=bool)
    roi_mask[y1:y1+roi_h, x1:x1+roi_w] = True
    skel_roi = skel & roi_mask

    _, num_comp = label(skel_roi, return_num=True)
    num_pix = np.sum(skel_roi)
    is_continuous = (num_comp == 1 and num_pix > 0)

    if is_continuous:
        status_msg = "PASS"
        title_color = "green"
    else:
        status_msg = f"FAIL (Comps: {num_comp})"
        title_color = "red"

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.imshow(bw, cmap='gray')
    ax.set_title(f"Status: {status_msg}", color=title_color, fontsize=16, fontweight='bold')
    
    rect = plt.Rectangle((x1, y1), roi_w, roi_h, linewidth=2, edgecolor='yellow', facecolor='none')
    ax.add_patch(rect)
    
    y_s, x_s = np.where(skel)
    ax.scatter(x_s, y_s, c='cyan', s=1, alpha=0.3)
    y_r, x_r = np.where(skel_roi)
    ax.scatter(x_r, y_r, c='red', s=5)

    skeleton_save_path = mask_path.replace("_MASK.PNG", "_SKELETON_RESULT.PNG")
    plt.savefig(skeleton_save_path)
    print(f" Saved Skeleton Plot: {skeleton_save_path}")

    print("   Opening Plot... Buzzing now...")
    plt.draw()
    plt.pause(0.1)
    
    if is_continuous: buzzer.beep_ok()
    else: buzzer.beep_fail()
        
    plt.show()

    return is_continuous

def _find_endpoints(skel):
    kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]], dtype=np.uint8)
    filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    return filtered == 11









##---------- WITHOUT FILTERING THE FLEX ----------------########


# import cv2
# import numpy as np
# import os
# import matplotlib.pyplot as plt
# from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_opening
# from scipy.ndimage import binary_fill_holes
# from skimage.measure import label
# import hardware.buzzer as buzzer

# def create_binary_mask(image_path):
    # print("🔍 [Vision] Step 2: Creating Binary Mask...")
    # img = cv2.imread(image_path)
    # if img is None: return None

    # # חיתוך ROI (חייב להיות זהה לצהוב)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    # roi_w = max(1, W // 8) # שים לב: כאן זה חלוקה ב-8 לפי הקוד הקודם שלך למסכות
    # roi_h = max(1, H // 8)
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    
    # roi_gray = gray[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()

    # DARK_THRESHOLD = 45 #35
    # _, dark_mask = cv2.threshold(roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

    # kernel = np.ones((3, 3), np.uint8)
    # mask_cleaned = cv2.morphologyEx(dark_mask, cv2.MORPH_OPEN, kernel)
    # mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)

    # # --- שמירה 3: המסכה הבינארית ---
    # dir_name = os.path.dirname(image_path)
    # base_name = os.path.basename(image_path)
    # name_no_ext = os.path.splitext(base_name)[0]
    
    # # השם יהיה למשל: corner_1_MASK.PNG
    # mask_path = os.path.join(dir_name, f"{name_no_ext}_MASK.PNG")
    
    # cv2.imwrite(mask_path, mask_final)
    # print(f"   💾 Saved Mask: {mask_path}")
    # return mask_path


# def check_skeleton_continuity(mask_path):
    # print("🔍 [Vision] Step 3: Checking Skeleton Continuity...")
    # if not mask_path or not os.path.exists(mask_path): return False

    # img = cv2.imread(mask_path, 0)
    # bw = img > 127
    # if np.mean(bw) > 0.5: bw = ~bw

    # bw = remove_small_objects(bw, min_size=500)
    # se = disk(8) #6
    # bw = binary_closing(bw, se)
    # bw = binary_opening(bw, se)
    # bw = binary_fill_holes(bw)
    # skel = skeletonize(bw)
    
    # for _ in range(10):
        # endpoints = _find_endpoints(skel)
        # skel[endpoints] = False

    # h, w = bw.shape
    # roi_frac = 0.80
    # roi_w = int(w * roi_frac)
    # roi_h = int(h * roi_frac)
    # x1 = (w - roi_w) // 2
    # y1 = (h - roi_h) // 2
    
    # roi_mask = np.zeros((h, w), dtype=bool)
    # roi_mask[y1:y1+roi_h, x1:x1+roi_w] = True
    # skel_roi = skel & roi_mask

    # _, num_comp = label(skel_roi, return_num=True)
    # num_pix = np.sum(skel_roi)
    # is_continuous = (num_comp == 1 and num_pix > 0)

    # if is_continuous:
        # status_msg = "PASS"
        # title_color = "green"
    # else:
        # status_msg = f"FAIL (Comps: {num_comp})"
        # title_color = "red"

    # # --- תצוגה ושמירה ---
    # fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    # ax.imshow(bw, cmap='gray')
    # ax.set_title(f"Status: {status_msg}", color=title_color, fontsize=16, fontweight='bold')
    
    # rect = plt.Rectangle((x1, y1), roi_w, roi_h, linewidth=2, edgecolor='yellow', facecolor='none')
    # ax.add_patch(rect)
    
    # y_s, x_s = np.where(skel)
    # ax.scatter(x_s, y_s, c='cyan', s=1, alpha=0.3)
    # y_r, x_r = np.where(skel_roi)
    # ax.scatter(x_r, y_r, c='red', s=5)

    # # --- שמירה 4: תמונת השלד ---
    # # מבוסס על שם המסכה (נחליף את _MASK ב-_SKELETON_RESULT)
    # # הנחה: mask_path מסתיים ב-_MASK.PNG
    # skeleton_save_path = mask_path.replace("_MASK.PNG", "_SKELETON_RESULT.PNG")
    # plt.savefig(skeleton_save_path)
    # print(f"   💾 Saved Skeleton Plot: {skeleton_save_path}")

    # print("   Opening Plot... Buzzing now...")
    # plt.draw()
    # plt.pause(0.1)
    
    # if is_continuous: buzzer.beep_ok()
    # else: buzzer.beep_fail()
        
    # plt.show()

    # return is_continuous

# def _find_endpoints(skel):
    # kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]], dtype=np.uint8)
    # filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    # return filtered == 11
