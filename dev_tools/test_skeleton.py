import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_opening
from scipy.ndimage import binary_fill_holes
from skimage.measure import label

# --- חלק 1: סימולציה של הבאזר (כדי שהקוד ירוץ בלי שגיאות חומרה) ---
class MockBuzzer:
    @staticmethod
    def beep_ok():
        print("\n[🔊 BUZZER] BEEP OK! (Continuous Skeleton) - צפצוף הצלחה")

    @staticmethod
    def beep_fail():
        print("\n[🔊 BUZZER] BEEP FAIL! (Broken Skeleton) - צפצוף כישלון")

# יצירת אובייקט באזר מדומה
buzzer = MockBuzzer()

# --- חלק 2: הפונקציות המקוריות שלך ---

def _find_endpoints(skel):
    """ פונקציית עזר למציאת קצוות בשלד """
    kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]], dtype=np.uint8)
    filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    return filtered == 11

def create_binary_mask(image_path):
    print(f"🔍 [Vision] Step 2: Creating Binary Mask for {os.path.basename(image_path)}...")
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Error: Could not load image. Check path.")
        return None

    # 1. חיתוך ROI
    H, W = img.shape[:2]
    roi_w = max(1, W // 5)
    roi_h = max(1, H // 5)
    x_start = (W - roi_w) // 2
    y_start = (H - roi_h) // 2
    
    roi_color = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    roi_gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)

    # 2. יצירת מסכה ראשונית
    DARK_THRESHOLD = 35 
    _, dark_mask = cv2.threshold(roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

    # 3. ניקוי ה-FLEX
    hsv = cv2.cvtColor(roi_color, cv2.COLOR_BGR2HSV)

    # טווח ירוק כהה
    lower_green = np.array([87, 101, 38])
    upper_green = np.array([96, 193, 60])
    mask_flex_green = cv2.inRange(hsv, lower_green, upper_green)

    # הרחבה קלה
    kernel_flex = np.ones((5, 5), np.uint8)
    flex_mask_total = cv2.dilate(mask_flex_green, kernel_flex, iterations=1)

    # מחיקת הפלקס מהמסכה הראשית
    dark_mask[flex_mask_total > 0] = 0

    # 4. חיתוך גיאומטרי (צד ימין)
    h_mask, w_mask = dark_mask.shape
    cutoff_x = int(w_mask * 0.85)
    dark_mask[:, cutoff_x:] = 0

    # 5. ניקוי מורפולוגי
    kernel_small = np.ones((5, 5), np.uint8)
    mask_pass1 = cv2.morphologyEx(dark_mask, cv2.MORPH_OPEN, kernel_small)
    mask_pass1 = cv2.morphologyEx(mask_pass1, cv2.MORPH_CLOSE, kernel_small)

    kernel_large = np.ones((5, 5), np.uint8)
    mask_pass2 = cv2.morphologyEx(mask_pass1, cv2.MORPH_OPEN, kernel_small)
    mask_final = cv2.morphologyEx(mask_pass2, cv2.MORPH_CLOSE, kernel_large)

    # שמירה
    dir_name = os.path.dirname(image_path)
    base_name = os.path.basename(image_path)
    name_no_ext = os.path.splitext(base_name)[0]
    
    mask_path = os.path.join(dir_name, f"{name_no_ext}_MASK.PNG")
    cv2.imwrite(mask_path, mask_final)
    
    print(f"✅ Saved Mask: {mask_path}")
    return mask_path

def check_skeleton_continuity(mask_path):
    print("🔍 [Vision] Step 3: Checking Skeleton Continuity...")
    if not mask_path or not os.path.exists(mask_path): 
        print("❌ Error: Mask path invalid.")
        return False

    img = cv2.imread(mask_path, 0)
    bw = img > 127
    if np.mean(bw) > 0.5: bw = ~bw

    bw = remove_small_objects(bw, min_size=500)
    se = disk(6)
    bw = binary_closing(bw, se)
    bw = binary_opening(bw, se)
    bw = binary_fill_holes(bw)
    skel = skeletonize(bw)
    
    # הסרת קצוות קטנים
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

    # תצוגה גרפית
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
    print(f"✅ Saved Skeleton Plot: {skeleton_save_path}")

    # לוגיקת באזר והצגה
    if is_continuous: 
        buzzer.beep_ok()
    else: 
        buzzer.beep_fail()
        
    print("Opening Plot window...")
    plt.show() # ה-show חייב להיות בסוף כדי להחזיק את החלון פתוח

    return is_continuous

# --- חלק 3: הרצה ראשית (Main) ---
if __name__ == "__main__":
    # ==========================================
    # הגדרות משתמש - שני כאן את הנתיב לתמונה שלך
    # ==========================================
    # דוגמה לנתיב (שימי לב להשתמש ב-/ או r"..." בווינדוס)
    IMAGE_PATH = "/home/pda-chipping/HQ_Camera_Codes_and_Pics/photo.PNG"  
    
    # ==========================================
    
    if os.path.exists(IMAGE_PATH):
        print(f" Starting process on: {IMAGE_PATH}")
        
        # שלב 1: יצירת מסכה
        generated_mask_path = create_binary_mask(IMAGE_PATH)
        
        # שלב 2: בדיקת שלד
        if generated_mask_path:
            result = check_skeleton_continuity(generated_mask_path)
            print(f"\n Final Result: {'PASS' if result else 'FAIL'}")
    else:
        print(f"❌ Error: Image not found at {IMAGE_PATH}")
        print("Please edit the 'IMAGE_PATH' variable in the script.")
