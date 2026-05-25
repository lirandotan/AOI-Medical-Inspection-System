import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_opening, thin
from skimage.measure import label, regionprops

def skeleton_large_blobs_center_roi(bw, roi_frac=0.60, min_area=500, smooth_radius=6, spur_iter=10, require_single_line=False):
	#def skeleton_large_blobs_center_roi(bw, roi_frac=0.60, min_area=5000, smooth_radius=6, spur_iter=20, require_single_line=False):
    """
    Python version of skeletonLargeBlobsCenterROI
    """
    # וודוא שהתמונה בולאנית
    bw = bw > 0

    # אם רוב הפיקסלים לבנים - היפוך (נחה שזה רקע)
    if np.mean(bw) > 0.5:
        bw = ~bw

    # 1) ניקוי גושים קטנים (בדומה ל-bwareaopen)
    bw1 = remove_small_objects(bw, min_size=min_area)

    # 2) החלקה מורפולוגית ומילוי חורים
    se = disk(smooth_radius)
    bw2 = binary_closing(bw1, se)
    bw2 = binary_opening(bw2, se)
    
    # מילוי חורים (בדומה ל-imfill)
    from scipy.ndimage import binary_fill_holes
    bw2 = binary_fill_holes(bw2)

    # 3) שלד (Skeletonization)
    # skimage משתמשת באלגוריתם Lee או Zhang-Suen
    skel = skeletonize(bw2)
    
    # Pruning (Spur) 
    # בפייתון אין "spur" ישיר כמו במטלב, נשתמש ב-thinning מספר פעמים או בפונקציית עזר
    skel_pruned = skel.copy()
    for _ in range(spur_iter):
        # מציאת נקודות קצה והסרתן
        endpoints = find_endpoints(skel_pruned)
        skel_pruned[endpoints] = False

    # 4) ROI מרכזי
    h, w = bw2.shape
    roi_w = max(5, int(round(w * roi_frac)))
    roi_h = max(5, int(round(h * roi_frac)))

    x1 = int(round((w - roi_w) / 2))
    y1 = int(round((h - roi_h) / 2))
    x2 = x1 + roi_w
    y2 = y1 + roi_h

    roi_mask = np.zeros((h, w), dtype=bool)
    roi_mask[y1:y2, x1:x2] = True

    skel_roi = skel_pruned & roi_mask

    # 5) בדיקת רציפות
    labeled_roi, num_comp = label(skel_roi, return_num=True)
    num_pix = np.sum(skel_roi)

    is_continuous = (num_comp == 1 and num_pix > 0)

    # בדיקת קו יחיד (2 נקודות קצה)
    is_single_line = True
    if require_single_line:
        ep_count = np.sum(find_endpoints(skel_roi))
        is_single_line = (ep_count == 2)

    is_ok = is_continuous and is_single_line

    # 6) הצגה (Matplotlib)
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax.imshow(bw2, cmap='gray')
    ax.set_title('Large blobs + skeleton + Center ROI continuity')

    # ציור ה-ROI
    rect = plt.Rectangle((x1, y1), roi_w, roi_h, linewidth=2, edgecolor='y', facecolor='none')
    ax.add_patch(rect)

    # ציור השלד
    y_s, x_s = np.where(skel_pruned)
    ax.scatter(x_s, y_s, c='cyan', s=1, label='Full Skeleton')

    # ציור השלד ב-ROI
    y_r, x_r = np.where(skel_roi)
    ax.scatter(x_r, y_r, c='red', s=5, label='ROI Skeleton')

    msg = "ROI skeleton: CONTINUOUS" if is_ok else "ROI skeleton: NOT continuous"
    ax.text(10, 30, msg, color='white', fontsize=12, fontweight='bold', bbox=dict(facecolor='black', alpha=0.5))

    plt.show()

    # 7) הדפסת דו"ח
    print(f"\n===== ROI Skeleton Continuity (Large Blobs) =====")
    print(f"ROI: x={x1}..{x2}, y={y1}..{y2} ({roi_frac*100:.0f}% of image)")
    print(f"Skeleton pixels in ROI: {num_pix}")
    print(f"Skeleton components in ROI: {num_comp}")
    print(f"Continuity: {'CONTINUOUS' if is_continuous else 'NOT continuous'}")
    
    if require_single_line:
        ep_count = np.sum(find_endpoints(skel_roi))
        print(f"Endpoints in ROI: {ep_count} (require 2) -> {'OK' if is_single_line else 'FAIL'}")

    return {
        "roi_rect": [x1, y1, roi_w, roi_h],
        "num_skel_pixels_roi": num_pix,
        "num_components_roi": num_comp,
        "is_continuous_roi": is_continuous,
        "is_single_line_roi": is_single_line,
        "is_ok": is_ok
    }

def find_endpoints(skel):
    """ פונקציית עזר למציאת נקודות קצה בשלד בינארי """
    # קונבולוציה פשוטה שסופרת שכנים
    kernel = np.array([[1, 1, 1],
                       [1, 10, 1],
                       [1, 1, 1]], dtype=np.uint8)
    filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    # נקודת קצה היא פיקסל דלוק (10) שיש לו בדיוק שכן אחד (1+10=11)
    return filtered == 11

# --- דוגמת הרצה ---
img = cv2.imread('/home/pda-chipping/HQ_Camera_Codes_and_Pics/output_mask/mask_test_FAIL.PNG', 0)
bw_input = img > 127
results = skeleton_large_blobs_center_roi(bw_input)





######--------------------------------------------------------------------------------------------#########



# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_dilation
# from skimage.measure import label
# from scipy.ndimage import binary_fill_holes

# def skeleton_large_blobs_center_roi(bw, roi_frac=0.6, min_area=500, connect_gap_size=5, spur_iter=30):
    # # וודוא שהתמונה בולאנית
    # bw = bw > 0
    # if np.mean(bw) > 0.5: bw = ~bw

    # # --- שלב הקסם: חיבור שברים אגרסיבי ---
    # # אנחנו משתמשים ב-Dilation כדי לנפח את הקווים עד שהם יגעו זה בזה
    # se_connect = disk(connect_gap_size)
    # bw_dilated = binary_dilation(bw, se_connect)
    
    # # מילוי חורים שנוצרו מהניפוח
    # bw_filled = binary_fill_holes(bw_dilated)

    # # ניקוי גושים קטנים שנשארו (עכשיו כשהם מחוברים, הגושים יהיו גדולים יותר)
    # bw_clean = remove_small_objects(bw_filled, min_size=min_area)

    # # --- יצירת שלד מהצורה המנופחת ---
    # skel = skeletonize(bw_clean)
    
    # # Pruning (ניקוי קוצים)
    # skel_pruned = skel.copy()
    # for _ in range(spur_iter):
        # endpoints = find_endpoints(skel_pruned)
        # skel_pruned[endpoints] = False

    # # --- ROI ובדיקת רציפות ---
    # h, w = bw.shape
    # roi_w, roi_h = int(w * roi_frac), int(h * roi_frac)
    # x1, y1 = int((w - roi_w) / 2), int((h - roi_h) / 2)
    
    # roi_mask = np.zeros_like(bw, dtype=bool)
    # roi_mask[y1:y1+roi_h, x1:x1+roi_w] = True
    # skel_roi = skel_pruned & roi_mask

    # labeled_roi, num_comp = label(skel_roi, return_num=True)
    # is_continuous = (num_comp == 1 and np.sum(skel_roi) > 0)

    # # הצגה
    # plt.figure(figsize=(10,7))
    # plt.imshow(bw_clean, cmap='gray') # מציג את התמונה אחרי החיבור
    # plt.title(f"After Connection (Gap Size: {connect_gap_size})")
    # rect = plt.Rectangle((x1, y1), roi_w, roi_h, edgecolor='y', facecolor='none', linewidth=2)
    # plt.gca().add_patch(rect)
    
    # y_r, x_r = np.where(skel_roi)
    # plt.scatter(x_r, y_r, c='red', s=5)
    # plt.show()

    # return is_continuous

# def find_endpoints(skel):
    # kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]], dtype=np.uint8)
    # filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    # return filtered == 11

# # הרצה עם הפרמטרים החדשים
# # res = skeleton_large_blobs_center_roi(BW, roi_frac=0.7, min_area=500, connect_gap_size=15)

# # --- דוגמת הרצה ---
# img = cv2.imread('/home/pda-chipping/HQ_Camera_Codes_and_Pics/output_mask/mask_test_FAIL.PNG', 0)
# bw_input = img > 127
# results = skeleton_large_blobs_center_roi(bw_input)


#####----------------------------------------------------------------------------------############


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from skimage.morphology import skeletonize, remove_small_objects, disk, binary_dilation
# from skimage.measure import label
# from scipy.ndimage import binary_fill_holes

# def skeleton_large_blobs_center_roi(bw, roi_frac=0.7, min_area=500, connect_gap_size=5, spur_iter=30, require_single_line=False):
    # # 1. הכנה והיפוך אם צריך
    # bw = bw > 0
    # if np.mean(bw) > 0.5: 
        # bw = ~bw

    # # 2. חיבור שברים (Dilation) ומילוי חורים
    # se_connect = disk(connect_gap_size)
    # bw_dilated = binary_dilation(bw, se_connect)
    # bw_filled = binary_fill_holes(bw_dilated)

    # # 3. ניקוי גושים קטנים
    # bw_clean = remove_small_objects(bw_filled, min_size=min_area)

    # # 4. יצירת שלד וניקוי קוצים (Pruning)
    # skel = skeletonize(bw_clean)
    # skel_pruned = skel.copy()
    # for _ in range(spur_iter):
        # endpoints = find_endpoints(skel_pruned)
        # skel_pruned[endpoints] = False

    # # 5. הגדרת ROI וגזירת השלד בתוכו
    # h, w = bw.shape
    # roi_w, roi_h = int(w * roi_frac), int(h * roi_frac)
    # x1, y1 = int((w - roi_w) / 2), int((h - roi_h) / 2)
    # x2, y2 = x1 + roi_w, y1 + roi_h
    
    # roi_mask = np.zeros_like(bw, dtype=bool)
    # roi_mask[y1:y2, x1:x2] = True
    # skel_roi = skel_pruned & roi_mask

    # # 6. חישוב מדדי רציפות
    # labeled_roi, num_comp = label(skel_roi, return_num=True)
    # num_pix = np.sum(skel_roi)
    # is_continuous = (num_comp == 1 and num_pix > 0)

    # # בדיקת קו יחיד (אופציונלי)
    # is_single_line = True
    # ep_roi_count = 0
    # if require_single_line:
        # ep_roi_count = np.sum(find_endpoints(skel_roi))
        # is_single_line = (ep_roi_count == 2)

    # is_ok = is_continuous and is_single_line

    # # 7. הצגה ויזואלית (כמו במטלב)
    # plt.figure(figsize=(10, 8))
    # plt.imshow(bw_clean, cmap='gray')
    # plt.title('Large blobs + skeleton + Center ROI continuity')

    # # ציור מסגרת ה-ROI (צהובה)
    # rect = plt.Rectangle((x1, y1), roi_w, roi_h, edgecolor='y', facecolor='none', linewidth=2)
    # plt.gca().add_patch(rect)

    # # ציור השלד המלא (בצבע תכלת/ציאן)
    # y_s, x_s = np.where(skel_pruned)
    # plt.scatter(x_s, y_s, c='cyan', s=1, label='Full Skeleton')

    # # ציור השלד ב-ROI (באדום מודגש)
    # y_r, x_r = np.where(skel_roi)
    # plt.scatter(x_r, y_r, c='red', s=8, label='ROI Skeleton')

    # # הוספת טקסט תוצאה על התמונה
    # msg = "ROI skeleton: CONTINUOUS" if is_ok else "ROI skeleton: NOT continuous"
    # color = "white"
    # plt.text(10, 30, msg, color=color, fontsize=14, fontweight='bold', 
             # bbox=dict(facecolor='red' if not is_ok else 'green', alpha=0.5))

    # plt.legend(loc='upper right')
    # plt.show()

    # # 8. הדפסת דו"ח למסך (כמו במטלב)
    # print(f"\n===== ROI Skeleton Continuity (Large Blobs) =====")
    # print(f"ROI: x={x1}..{x2}, y={y1}..{y2} ({roi_frac*100:.0f}% of image)")
    # print(f"Skeleton pixels in ROI: {num_pix}")
    # print(f"Skeleton components in ROI: {num_comp}")
    # print(f"Continuity: {'CONTINUOUS' if is_continuous else 'NOT continuous'}")
    
    # if require_single_line:
        # print(f"Endpoints in ROI: {ep_roi_count} (require 2) -> {'OK' if is_single_line else 'FAIL'}")
    
    # print(f"FINAL DIAGNOSIS: {'OK' if is_ok else 'FAIL'}")

    # # החזרת תוצאות במילון (struct)
    # return {
        # "roiRect": [x1, y1, roi_w, roi_h],
        # "numSkelPixelsROI": num_pix,
        # "numComponentsROI": num_comp,
        # "isContinuousROI": is_continuous,
        # "isSingleLineROI": is_single_line,
        # "isOK": is_ok
    # }

# def find_endpoints(skel):
    # """ מוצא נקודות קצה בשלד בינארי """
    # kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]], dtype=np.uint8)
    # filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    # return filtered == 11

# # --- הרצה ---
# img_path = '/home/pda-chipping/HQ_Camera_Codes_and_Pics/output_mask1/mask_0501263.PNG'
# img = cv2.imread(img_path, 0)
# if img is not None:
    # bw_input = img > 127
    # # שימי לב: אפשר לשנות את connect_gap_size ל-7 או 10 אם הקו עדיין נראה שבור
    # res = skeleton_large_blobs_center_roi(bw_input, roi_frac=0.7, connect_gap_size=5, spur_iter=30)
# else:
    # print("Error: Image not found.")


#########---------------ON FOLDER ------------------------###################################


# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import os
# import glob
# from skimage.morphology import skeletonize, remove_small_objects, disk, binary_closing, binary_opening
# from skimage.measure import label
# from scipy.ndimage import binary_fill_holes

# # ==========================================
# # 1. פונקציות עזר (Logic)
# # ==========================================

# def find_endpoints(skel):
    # """ פונקציית עזר למציאת נקודות קצה בשלד בינארי """
    # kernel = np.array([[1, 1, 1],
                       # [1, 10, 1],
                       # [1, 1, 1]], dtype=np.uint8)
    # filtered = cv2.filter2D(skel.astype(np.uint8), -1, kernel)
    # return filtered == 11

# #def skeleton_large_blobs_center_roi(bw, save_path=None, roi_frac=0.70, min_area=4000, smooth_radius=8, spur_iter=10, require_single_line=False):
# def skeleton_large_blobs_center_roi(bw, save_path=None, roi_frac=0.60, min_area=500, smooth_radius=12, spur_iter=10, require_single_line=False):	
    # """
    # מבצע עיבוד, ואם save_path מוגדר - שומר את התמונה עם הסימונים לדיסק.
    # """
    # # וודוא שהתמונה בולאנית
    # bw = bw > 0

    # # היפוך אם צריך
    # if np.mean(bw) > 0.5:
        # bw = ~bw

    # # 1) ניקוי והחלקה
    # bw1 = remove_small_objects(bw, min_size=min_area)
    # se = disk(smooth_radius)
    # bw2 = binary_closing(bw1, se)
    # bw2 = binary_opening(bw2, se)
    # bw2 = binary_fill_holes(bw2)

    # # 2) שלד
    # skel = skeletonize(bw2)
    
    # # Pruning
    # skel_pruned = skel.copy()
    # for _ in range(spur_iter):
        # endpoints = find_endpoints(skel_pruned)
        # skel_pruned[endpoints] = False

    # # 3) ROI
    # h, w = bw2.shape
    # roi_w = max(5, int(round(w * roi_frac)))
    # roi_h = max(5, int(round(h * roi_frac)))
    # x1 = int(round((w - roi_w) / 2))
    # y1 = int(round((h - roi_h) / 2))
    # x2 = x1 + roi_w
    # y2 = y1 + roi_h

    # roi_mask = np.zeros((h, w), dtype=bool)
    # roi_mask[y1:y2, x1:x2] = True
    # skel_roi = skel_pruned & roi_mask

    # # 4) בדיקות
    # labeled_roi, num_comp = label(skel_roi, return_num=True)
    # num_pix = np.sum(skel_roi)
    # is_continuous = (num_comp == 1 and num_pix > 0)

    # is_single_line = True
    # if require_single_line:
        # ep_count = np.sum(find_endpoints(skel_roi))
        # is_single_line = (ep_count == 2)

    # is_ok = is_continuous and is_single_line

    # # 5) שמירת תמונה לדיסק (במקום להציג למסך)
    # if save_path is not None:
        # # יצירת Figure ללא הצגה מיידית
        # fig, ax = plt.subplots(1, 1, figsize=(10, 8))
        # ax.imshow(bw2, cmap='gray')
        
        # # כותרת צבעונית בהתאם לתוצאה
        # title_color = 'green' if is_ok else 'red'
        # status_text = "PASS" if is_ok else "FAIL"
        # ax.set_title(f'Status: {status_text} (Comps: {num_comp})', color=title_color, fontsize=16, fontweight='bold')

        # # ציור ROI
        # rect = plt.Rectangle((x1, y1), roi_w, roi_h, linewidth=2, edgecolor='y', facecolor='none')
        # ax.add_patch(rect)

        # # ציור השלד בתוך ה-ROI באדום
        # y_r, x_r = np.where(skel_roi)
        # ax.scatter(x_r, y_r, c='red', s=5, label='ROI Skeleton')

        # # ציור שאר השלד בתכלת עדין
        # y_s, x_s = np.where(skel_pruned & ~roi_mask)
        # ax.scatter(x_s, y_s, c='cyan', s=1, alpha=0.3)

        # # שמירה וסגירה (כדי לא לפוצץ זיכרון)
        # plt.savefig(save_path)
        # plt.close(fig) 

    # return {
        # "is_ok": is_ok,
        # "num_components_roi": num_comp
    # }

# # ==========================================
# # 2. הרצה ראשית
# # ==========================================

# def main():
    # # נתיב הקלט
    # input_folder = '/home/pda-chipping/HQ_Camera_Codes_and_Pics/output_mask1/'
    
    # # נתיב הפלט (ייצור תיקייה חדשה בתוך התיקייה הנוכחית)
    # output_folder = os.path.join(input_folder, 'results_view')
    # if not os.path.exists(output_folder):
        # os.makedirs(output_folder)
        # print(f"Created output directory: {output_folder}")

    # # איסוף קבצים
    # extensions = ['*.PNG', '*.png', '*.JPG', '*.jpg']
    # files_list = []
    # for ext in extensions:
        # files_list.extend(glob.glob(os.path.join(input_folder, ext)))
    
    # files_list.sort()
    
    # print(f"Processing {len(files_list)} images...")
    # print(f"Results will be saved to: {output_folder}\n")

    # count_pass = 0
    # count_fail = 0

    # for file_path in files_list:
        # file_name = os.path.basename(file_path)
        
        # # דילוג על קבצים שכבר עובדו כדי לא לנתח את התוצאות של עצמנו
        # if "result_" in file_name:
            # continue

        # img = cv2.imread(file_path, 0)
        # if img is None:
            # continue

        # bw_input = img > 127
        
        # # שם הקובץ לשמירה
        # save_name = f"result_{'PASS' if True else 'FAIL'}_{file_name}" 
        # # (אנחנו עדיין לא יודעים אם זה PASS או FAIL לפני הריצה, אז נשמור עם השם המקורי ונוסיף פרדקיס בסוף אם תרצה, אבל הכי פשוט לשמור בשם המקורי)
        # save_full_path = os.path.join(output_folder, f"res_{file_name}")

        # # הרצה ושמירה
        # res = skeleton_large_blobs_center_roi(bw_input, save_path=save_full_path)
        
        # status = "PASS" if res['is_ok'] else "FAIL"
        
        # # הדפסה לוג בטרמינל
        # print(f"Saved: {file_name:<30} -> {status}")

        # if res['is_ok']:
            # count_pass += 1
        # else:
            # count_fail += 1

    # print("-" * 50)
    # print(f"Done. Check the folder: {output_folder}")
    # print(f"PASS: {count_pass}, FAIL: {count_fail}")

# if __name__ == "__main__":
    # main()
