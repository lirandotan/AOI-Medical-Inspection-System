
# #####-------------MASK - GOOD BUT NEED ANALYZE AND MORE------------------------------------------------------######

# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt

# # --- Tuned global parameters ---
# # Variance threshold above which the PDA is considered defective
# # Grayscale threshold used to isolate dark PDA material
# FINAL_VARIANCE_THRESHOLD = 250
# DARK_THRESHOLD = 35

# # --- Centered ROI parameters ---
# # Dividing image dimensions by 3 results in a centered ROI
# # with ~1/9 of the total image area
# ROI_DIVISOR = 8 

# # --- NEW: הגדרת נתיבי תיקיות לשמירה ---##
# ROI_OUTPUT_DIR = "output_roi"
# MASK_OUTPUT_DIR = "output_mask"

# # יצירת התיקיות במידה והן לא קיימות
# if not os.path.exists(ROI_OUTPUT_DIR):
    # os.makedirs(ROI_OUTPUT_DIR)
# if not os.path.exists(MASK_OUTPUT_DIR):
    # os.makedirs(MASK_OUTPUT_DIR)
    
# ##---------------------------------##
    
# def analyze_pda_integrity_final_optimized(image_path, debug=False):
    # """
    # Analyze a PDA image to detect chipping/cracks
    # using a centered and reduced ROI.
    # Returns True if component is GOOD, False if DEFECTIVE.
    # """
    
    # # 1. Load image from disk
   
    # img = cv2.imread(image_path)

    # if img is None:
        # print(f"❌ Error: Could not load image at {image_path}")
        # return False
        
    # # Convert image to grayscale
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # # Extract image dimensions
    # H, W = gray.shape
    
    # # 2. Compute centered and reduced ROI dimensions
    # # ROI width and height (1/3 of full image size)
    # roi_w = max(1, W // ROI_DIVISOR)
    # roi_h = max(1, H // ROI_DIVISOR)
    
    # # Compute top-left corner for centered ROI
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    # x_end = x_start + roi_w
    # y_end = y_start + roi_h
    
    # # Crop the ROI from both color and grayscale images
    # critical_roi_color = img[y_start:y_end, x_start:x_end].copy()
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # # Safety check: ensure ROI is valid
    # if critical_roi_gray.size == 0:
        # print("⚠️ Warning: Centered ROI size is zero.")
        # return False
        
    # # 3. Create PDA mask by thresholding dark pixels
    # # PDA material is expected to be darker than background
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # --- NEW: שמירת הקבצים ---
    # # חילוץ שם הקובץ המקורי (למשל: image1.png)
    # file_name = os.path.basename(image_path)
    
    # # יצירת נתיב מלא לשמירה
    # roi_save_path = os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}")
    # mask_save_path = os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}")
    
    # # שמירה פיזית לכונן
    # cv2.imwrite(roi_save_path, critical_roi_color)
    # cv2.imwrite(mask_save_path, dark_pda_mask)
    # ##---------------------------------##

    
   # # 4. Variance analysis on PDA pixels only
    # # Extract grayscale values only where PDA mask is active
    # pda_pixels = critical_roi_gray[dark_pda_mask == 255]
    # # If too few pixels are detected, force a high variance
    # # to avoid false "GOOD" classification
    # if pda_pixels.size < 50: 
         # variance = 5000 
    # else:
       # # Compute pixel intensity variance
       # # Defects introduce texture and brightness fluctuations
        # variance = np.var(pda_pixels)
    
    # # 5. Final decision
        # is_defective = variance > FINAL_VARIANCE_THRESHOLD

        # if debug:
            # print(f"--- {file_name} ---")
            # # כל מה שמתחת ל-debug חייב להיות מוסט פנימה
            # img_debug = img.copy()
            # cv2.rectangle(img_debug, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
            # # ... שאר קוד הציור ...
            # plt.show()

        # # השורה הזו חייבת להיות בקו של ה-if debug
        # return not is_defective    
    # # if debug:
        # # print(f"--- {os.path.basename(image_path)} ---")
        # # print(f"Optimized ROI: ({x_start}, {y_start}) to ({x_end}, {y_end}). Size: {roi_w}x{roi_h}")
        # # print(f"Calculated Variance in PDA Pixels: {variance:.2f} (Threshold: {FINAL_VARIANCE_THRESHOLD})")
        
        # # # Draw ROI on original image for visualization
        # # img_debug = img.copy()
        # # cv2.rectangle(img_debug, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
               
        # # # Overlay classification result text
        # # result_text = "❌ DEFECTIVE" if is_defective else "✅ GOOD"
        # # cv2.putText(img_debug, result_text, (x_start, y_start - 10), 
                    # # cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255) if is_defective else (0, 255, 0), 2)
       
        # # # Display debug visualization
        # # plt.figure(figsize=(12, 5))
        # # plt.subplot(131), plt.imshow(cv2.cvtColor(img_debug, cv2.COLOR_BGR2RGB)), plt.title('Original + Optimized ROI')
        # # plt.subplot(132), plt.imshow(critical_roi_gray, cmap='gray'), plt.title('Critical ROI (Gray)')
        # # plt.subplot(133), plt.imshow(dark_pda_mask, cmap='gray'), plt.title(f'PDA Mask (Var: {variance:.0f})')
        # # plt.show()

    # # # Return True if component is GOOD  
    # # return not is_defective

# # --- הגדרת נתיבי התמונות המדויקים (כפי שסופקו) ---

# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",     
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",     
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",          
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"            
# ]

# # --- הרצה ---
# if __name__ == "__main__":
    
    # # ודא שהפונקציה analyze_pda_integrity_final_optimized מוגדרת וזמינה
    
    # print("--- בדיקת רכיבים פגומים (צפוי: ❌ DEFECTIVE) ---")
    # for img_path in defective_images:
        
        # # 🟢 התיקון: שימוש ישיר בנתיב ה-.PNG שסופק
        # path_to_use = img_path 
        
        # # אם התמונות שלך הן באמת JPG, הסר את כל ה-.PNG מהרשימה
        # # אם הן PNG, התיקון הזה עובד.

        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"{os.path.basename(path_to_use)}: {status}")

    # print("\n--- בדיקת רכיבים תקינים (צפוי: ✅ GOOD) ---")
    # for img_path in good_images:
        
        # # 🟢 התיקון: שימוש ישיר בנתיב ה-.PNG שסופק
        # path_to_use = img_path
        
        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"{os.path.basename(path_to_use)}: {status}")
        
######--------------------------------------------------------------------------------------------------------------###
        
        
###----------------------------MASK GOOD - WITH OPEN CLOSE -------------------------------------------------------------####

        
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

# --- Tuned global parameters ---
# Variance threshold above which the PDA is considered defective
# Grayscale threshold used to isolate dark PDA material
FINAL_VARIANCE_THRESHOLD = 42
DARK_THRESHOLD = 35

# --- Centered ROI parameters ---
# Dividing image dimensions by 3 results in a centered ROI
# with ~1/9 of the total image area
ROI_DIVISOR = 8 

# --- NEW: הגדרת נתיבי תיקיות לשמירה ---##
ROI_OUTPUT_DIR = "output_roi1"
MASK_OUTPUT_DIR = "output_mask1"

# יצירת התיקיות במידה והן לא קיימות
if not os.path.exists(ROI_OUTPUT_DIR):
    os.makedirs(ROI_OUTPUT_DIR)
if not os.path.exists(MASK_OUTPUT_DIR):
    os.makedirs(MASK_OUTPUT_DIR)
    
##---------------------------------##
    
def analyze_pda_integrity_final_optimized(image_path, debug=False):
    """
    Analyze a PDA image to detect chipping/cracks
    using a centered and reduced ROI.
    Returns True if component is GOOD, False if DEFECTIVE.
    """
    
    # 1. Load image from disk
    img = cv2.imread(image_path)

    if img is None:
        print(f"❌ Error: Could not load image at {image_path}")
        return False
        
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Extract image dimensions
    H, W = gray.shape
    
    # 2. Compute centered and reduced ROI dimensions
    # ROI width and height (1/3 of full image size)
    roi_w = max(1, W // ROI_DIVISOR)
    roi_h = max(1, H // ROI_DIVISOR)
    
    # Compute top-left corner for centered ROI
    x_start = (W - roi_w) // 2
    y_start = (H - roi_h) // 2
    x_end = x_start + roi_w
    y_end = y_start + roi_h
    
    # Crop the ROI from both color and grayscale images
    critical_roi_color = img[y_start:y_end, x_start:x_end].copy()
    critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # Safety check: ensure ROI is valid
    if critical_roi_gray.size == 0:
        print("⚠️ Warning: Centered ROI size is zero.")
        return False
        
    # 3. Create PDA mask by thresholding dark pixels
    # PDA material is expected to be darker than background
    _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
   # ... (המשך מקודם: אחרי יצירת dark_pda_mask) ...

    # 1. שלב ראשון: ניקוי רעשים (OPEN)
    # משתמשים בקרנל קטן ועדין כדי לא לפגוע בצורה, רק להעיף לכלוך
    kernel = np.ones((3, 3), np.uint8) 
    mask_cleaned = cv2.morphologyEx(dark_pda_mask, cv2.MORPH_OPEN, kernel)
    
    # 2. שלב שני: סתימת חורים (CLOSE)
    # עכשיו כשהשטח נקי, משתמשים בקרנל גדול ואגרסיבי כדי לסתום את כל החורים השחורים בתוך הלבן
    mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)

    # ... (ממשיכים לשמירה וניתוח עם mask_final) ...
    # ----------------------------------------------------

    # --- NEW: שמירת הקבצים ---
    # חילוץ שם הקובץ המקורי (למשל: image1.png)
    file_name = os.path.basename(image_path)
    
    # יצירת נתיב מלא לשמירה
    roi_save_path = os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}")
    mask_save_path = os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}")
    
    # שמירה פיזית לכונן
    cv2.imwrite(roi_save_path, critical_roi_color)
    
    # שים לב: אנחנו שומרים כעת את mask_final (הנקייה) ולא את המקורית
    cv2.imwrite(mask_save_path, mask_final)
    ##---------------------------------##

    
   # 4. Variance analysis on PDA pixels only
    # Extract grayscale values only where CLEANED PDA mask is active
    pda_pixels = critical_roi_gray[mask_final == 255]
    
    # If too few pixels are detected, force a high variance
    # to avoid false "GOOD" classification
    if pda_pixels.size < 50: 
          variance = 5000 
    else:
       # Compute pixel intensity variance
       # Defects introduce texture and brightness fluctuations
        variance = np.var(pda_pixels)
    
    # 5. Final decision
    is_defective = variance > FINAL_VARIANCE_THRESHOLD

    if debug:
        print(f"--- {file_name} ---")
        img_debug = img.copy()
        cv2.rectangle(img_debug, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
        # plt.show() # הוסר זמנית כדי לא לעצור את הריצה, ניתן להחזיר

    # Return True if component is GOOD    
    return not is_defective

# --- הגדרת נתיבי התמונות המדויקים (כפי שסופקו) ---

defective_images = [
    "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",     
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG", 
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/test.PNG", 
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/0501261.PNG" ,
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/0501263.PNG"  
]

good_images = [
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG" ,
    "/home/pda-chipping/HQ_Camera_Codes_and_Pics/good.PNG"             
]

# --- הרצה ---
if __name__ == "__main__":
    
    print("--- בדיקת רכיבים פגומים (צפוי: ❌ DEFECTIVE) ---")
    for img_path in defective_images:
        
        path_to_use = img_path 
        
        # הרצת הפונקציה
        is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        print(f"{os.path.basename(path_to_use)}: {status}")

    print("\n--- בדיקת רכיבים תקינים (צפוי: ✅ GOOD) ---")
    for img_path in good_images:
        
        path_to_use = img_path
        
        # הרצת הפונקציה
        is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        print(f"{os.path.basename(path_to_use)}: {status}")
        
    
    
    
######---------------------ONE_PIC---------------------------------------------------------------------###

# import cv2
# import numpy as np
# import os

# # --- הפרמטרים מהקוד המקורי ---
# DARK_THRESHOLD = 35

# def convert_to_binary_and_save(image_path):
    # """
    # טוען תמונה, ממיר לבינארי (עם ניקוי רעשים) ושומר באותה תיקייה.
    # """
    # # 1. טעינת התמונה
    # img = cv2.imread(image_path)
    
    # if img is None:
        # print(f"❌ שגיאה: לא ניתן לטעון את התמונה בנתיב: {image_path}")
        # return

    # # 2. המרה לאפור
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # # 3. יצירת מסכה בינארית (Threshold)
    # # שימוש ב-THRESH_BINARY_INV הופך את הכהה (ה-PDA) ללבן (255) ואת הרקע לשחור (0)
    # _, binary_mask = cv2.threshold(gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # 4. פעולות מורפולוגיות (בדיוק כמו בקוד המקורי)
    # kernel = np.ones((3, 3), np.uint8) 
    
    # # שלב ראשון: ניקוי רעשים (OPEN)
    # mask_cleaned = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)
    
    # # שלב שני: סתימת חורים (CLOSE)
    # mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)

    # # 5. שמירה באותה תיקייה של המקור
    # # שליפת הנתיב של התיקייה המקורית ושם הקובץ
    # dir_name = os.path.dirname(image_path)
    # file_name = os.path.basename(image_path)
    # name_without_ext, ext = os.path.splitext(file_name)
    
    # # יצירת שם חדש: original_name_binary.PNG
    # new_file_name = f"{name_without_ext}_binary{ext}"
    # save_path = os.path.join(dir_name, new_file_name)
    
    # # שמירה
    # cv2.imwrite(save_path, mask_final)
    # print(f"✅ נשמר: {save_path}")

# # --- רשימת התמונות שלך ---
# image_list = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/0501261_ROI4.PNG"

# ]

# # --- הרצה ---
# if __name__ == "__main__":
    # print("--- מתחיל עיבוד ושמירת תמונות בינאריות ---")
    # for img_path in image_list:
        # convert_to_binary_and_save(img_path)




    
        
###----------MASK GOOD - WITH OPEN CLOSE AND Hough Transform (lines) - TO CHECK------------------------------------##########
        
# import cv2
# import numpy as np
# import os
# import math  # <--- הוספה: נדרש לחישוב הזוויות
# from matplotlib import pyplot as plt

# # --- Tuned global parameters ---
# FINAL_VARIANCE_THRESHOLD = 42
# DARK_THRESHOLD = 35
# ROI_DIVISOR = 8 

# # --- הגדרת נתיבי תיקיות לשמירה ---
# ROI_OUTPUT_DIR = "output_roi"
# MASK_OUTPUT_DIR = "output_mask"

# if not os.path.exists(ROI_OUTPUT_DIR):
    # os.makedirs(ROI_OUTPUT_DIR)
# if not os.path.exists(MASK_OUTPUT_DIR):
    # os.makedirs(MASK_OUTPUT_DIR)
    
# # =========================================================
# # --- פונקציות עזר חדשות (גיאומטריה וקווים) ---
# # =========================================================

# def calculate_angle(line1, line2):
    # """
    # מקבל שני קווים ומחשב את הזווית ביניהם במעלות.
    # """
    # # חילוץ הקואורדינטות של הקו הראשון והשני
    # x1, y1, x2, y2 = line1[0]
    # x3, y3, x4, y4 = line2[0]
    
    # # חישוב הוקטורים של הקווים
    # vector1 = (x2 - x1, y2 - y1)
    # vector2 = (x4 - x3, y4 - y3)
    
    # # חישוב מכפלה סקלרית (Dot Product)
    # dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    
    # # חישוב אורך (Magnitude) של כל וקטור
    # magnitude1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    # magnitude2 = math.sqrt(vector2[0]**2 + vector2[1]**2)
    
    # if magnitude1 == 0 or magnitude2 == 0:
        # return 0
        
    # # חישוב הזווית בעזרת arccos
    # cos_angle = dot_product / (magnitude1 * magnitude2)
    # # תיקון שגיאות נומריות קטנות (לוודא שנשארים בין -1 ל 1)
    # cos_angle = max(-1.0, min(1.0, cos_angle))
    
    # angle_rad = math.acos(cos_angle)
    # angle_deg = math.degrees(angle_rad)
    
    # return angle_deg

# def check_corner_geometry(binary_mask, debug_img=None):
    # """
    # גרסה 12 (Back to Basics): חזרה לגרסה 10 שעבדה מצוין,
    # אך עם בדיקה בטווח רחוק (Long Range) כדי לתפוס שברים גדולים.
    # """
    # # 1. מציאת קונטור חיצוני
    # contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if not contours: return False, 0
    
    # c = max(contours, key=cv2.contourArea)
    # points = c[:, 0, :] # [x, y]
    
    # # 2. מציאת ה"שפיץ" - הנקודה הכי שמאלית
    # leftmost_idx = np.argmin(points[:, 0])
    # tip_pt = points[leftmost_idx]
    # tip_x, tip_y = tip_pt[0], tip_pt[1]
    
    # # 3. הגדרת נקודות בדיקה (Probes) - השינוי הגדול!
    # # במקום 30, אנחנו בודקים במרחק 75 פיקסלים.
    # # זה מבטיח שאנחנו בודקים את הקירות האמיתיים ולא שבר מקומי.
    # offset_y = 75
    # target_y_up = tip_y - offset_y
    # target_y_down = tip_y + offset_y
    
    # # פונקציית עזר למציאת X בגובה מסוים
    # def get_x_at_y(target_y):
        # # מחפשים נקודות בטווח Y קרוב
        # indices = np.where((points[:, 1] >= target_y - 2) & (points[:, 1] <= target_y + 2))
        # if len(indices[0]) == 0: return None
        # return np.min(points[indices[0]][:, 0])

    # x_up = get_x_at_y(target_y_up)
    # x_down = get_x_at_y(target_y_down)
    
    # # מנגנון גיבוי: אם התמונה חתוכה ואין נקודות במרחק 75, ננסה 50
    # if x_up is None or x_down is None:
        # offset_y = 50
        # target_y_up = tip_y - offset_y
        # target_y_down = tip_y + offset_y
        # x_up = get_x_at_y(target_y_up)
        # x_down = get_x_at_y(target_y_down)

    # # אם עדיין לא מצאנו (רכיב קטנטן או שבור לגמרי), נכשיל
    # if x_up is None or x_down is None:
        # return False, 0

    # # 4. חישוב החדות (Sharpness / Retreat)
    # # כמה הקיר "בורח" ימינה ביחס לשפיץ?
    # diff_up = x_up - tip_x
    # diff_down = x_down - tip_x
    
    # total_sharpness = diff_up + diff_down
    
    # # 5. החלטה סופית
    # # בגלל שהגדלנו את הטווח, המספרים יהיו גדולים יותר.
    # # פינה יפה תתן מספרים באזור 60-100.
    # # שבר שטוח יתן מספרים נמוכים (מתחת ל-25).
    # is_good = total_sharpness > 25
    
    # # 6. ציור לדיבאג
    # if debug_img is not None:
        # # השפיץ
        # cv2.circle(debug_img, (tip_x, tip_y), 8, (0, 255, 0), -1)
        # # נקודות הבדיקה
        # cv2.circle(debug_img, (x_up, target_y_up), 5, (255, 0, 0), -1)
        # cv2.circle(debug_img, (x_down, target_y_down), 5, (255, 0, 0), -1)
        
        # # המשולש
        # pts_triangle = np.array([[tip_x, tip_y], [x_up, target_y_up], [x_down, target_y_down]], np.int32)
        # color = (0, 255, 0) if is_good else (0, 0, 255)
        # cv2.polylines(debug_img, [pts_triangle], True, color, 2)
        
        # label = f"Score: {total_sharpness}"
        # cv2.putText(debug_img, label, (tip_x + 20, tip_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    # return is_good, total_sharpness

# # =========================================================
# # --- הפונקציה הראשית המעודכנת ---
# # =========================================================
    
# def analyze_pda_integrity_final_optimized(image_path, debug=False):
    # """
    # Analyze a PDA image to detect chipping/cracks
    # using Variance (Texture) AND Geometry (Lines).
    # """
    
    # # 1. Load image
    # img = cv2.imread(image_path)
    # if img is None:
        # print(f"❌ Error: Could not load image at {image_path}")
        # return False
        
    # # Convert and Crop
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    # x_end, y_end = x_start + roi_w, y_start + roi_h
    
    # critical_roi_color = img[y_start:y_end, x_start:x_end].copy()
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # if critical_roi_gray.size == 0:
        # return False
        
    # # 3. Create Mask
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # --- UPDATED MORPHOLOGY: OPEN THEN CLOSE ---
    # # שלב 1: OPEN - ניקוי שוליים (מיישר את הקווים לזיהוי זווית טוב יותר)
    # kernel_clean = np.ones((3, 3), np.uint8) 
    # mask_cleaned = cv2.morphologyEx(dark_pda_mask, cv2.MORPH_OPEN, kernel_clean)
    
    # # שלב 2: CLOSE - סתימת חורים פנימיים (קרנל גדול)
    # kernel_fill = np.ones((3, 3), np.uint8)
    # mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel_fill)
    # # -------------------------------------------

    # # שמירת קבצים
    # file_name = os.path.basename(image_path)
    # roi_save_path = os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}")
    # mask_save_path = os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}")
    # cv2.imwrite(roi_save_path, critical_roi_color)
    # cv2.imwrite(mask_save_path, mask_final)

    
    # # --- ANALYSIS PART 1: TEXTURE (Variance) ---
    # pda_pixels = critical_roi_gray[mask_final == 255]
    
    # if pda_pixels.size < 50: 
          # variance = 5000 
    # else:
        # variance = np.var(pda_pixels)
    
    # # בדיקה 1: האם הטקסטורה חלקה?
    # is_texture_good = variance < FINAL_VARIANCE_THRESHOLD

    # # --- ANALYSIS PART 2: GEOMETRY (Lines & Angle) ---
    # # אנו שולחים עותק של התמונה הצבעונית כדי לצייר עליו את הקווים לדיבאג
    # img_for_lines = critical_roi_color.copy()
    # is_geometry_good, angle_found = check_corner_geometry(mask_final, img_for_lines)
    
    # # --- FINAL DECISION ---
    # # הרכיב תקין רק אם: הטקסטורה טובה (אין שריטות) וגם הגיאומטריה טובה (יש פינה)
    # is_good = is_texture_good and is_geometry_good

    # if debug:
        # print(f"--- {file_name} ---")
        # print(f"   [Texture] Variance: {variance:.2f} (Limit: {FINAL_VARIANCE_THRESHOLD}) -> {'OK' if is_texture_good else 'FAIL'}")
        # print(f"   [Geometry] Angle: {angle_found:.2f}° (Target: ~90°) -> {'OK' if is_geometry_good else 'FAIL'}")
        
        # # ויזואליזציה: מראה גם את המסכה וגם את הקווים שזוהו
        # plt.figure(figsize=(10, 4))
        # plt.subplot(121), plt.imshow(mask_final, cmap='gray'), plt.title('Final Mask')
        # plt.subplot(122), plt.imshow(cv2.cvtColor(img_for_lines, cv2.COLOR_BGR2RGB)), plt.title(f'Detected Lines (Angle: {angle_found:.1f})')
        # plt.show()

    # return is_good

# # --- נתיבי התמונות ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",     
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",     
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# # --- הרצה ---
# if __name__ == "__main__":
    
    # print("--- בדיקת רכיבים פגומים (צפוי: ❌ DEFECTIVE) ---")
    # for img_path in defective_images:
        # path_to_use = img_path 
        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"RESULT: {os.path.basename(path_to_use)}: {status}\n")

    # print("\n--- בדיקת רכיבים תקינים (צפוי: ✅ GOOD) ---")
    # for img_path in good_images:
        # path_to_use = img_path
        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"RESULT: {os.path.basename(path_to_use)}: {status}\n")



#####----------------------Mask and BASIC Skeletonization for PDA Defect Detection -------------------------------------#####

# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt

# # --- Tuned global parameters (מהקוד המקורי שלך) ---
# FINAL_VARIANCE_THRESHOLD = 250
# DARK_THRESHOLD = 35
# ROI_DIVISOR = 8 

# # --- נתיבי תיקיות ---
# ROI_OUTPUT_DIR = "output_roi"
# MASK_OUTPUT_DIR = "output_mask"
# SKELETON_OUTPUT_DIR = "output_skeleton_basic"

# if not os.path.exists(ROI_OUTPUT_DIR): os.makedirs(ROI_OUTPUT_DIR)
# if not os.path.exists(MASK_OUTPUT_DIR): os.makedirs(MASK_OUTPUT_DIR)
# if not os.path.exists(SKELETON_OUTPUT_DIR): os.makedirs(SKELETON_OUTPUT_DIR)
    
# def get_basic_skeleton(binary_img):
    # """
    # האלגוריתם הקלאסי והבסיסי ביותר של OpenCV לשילוד.
    # בלי שום סינונים ובלי תחכום.
    # """
    # img = binary_img.copy()
    # skel = np.zeros(img.shape, np.uint8)
    # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    
    # while True:
        # open_op = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        # temp = cv2.subtract(img, open_op)
        # eroded = cv2.erode(img, element)
        # skel = cv2.bitwise_or(skel, temp)
        # img = eroded.copy()
        
        # if cv2.countNonZero(img) == 0:
            # break
            
    # return skel

# def analyze_pda_basic(image_path, debug=False):
    
    # # 1. טעינה וחיתוך (בדיוק כמו בקוד המקורי)
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    
    # roi_w = max(1, W // ROI_DIVISOR)
    # roi_h = max(1, H // ROI_DIVISOR)
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    # x_end = x_start + roi_w
    # y_end = y_start + roi_h
    
    # critical_roi_color = img[y_start:y_end, x_start:x_end].copy()
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # if critical_roi_gray.size == 0: return False
        
    # # 2. יצירת מסכה (בדיוק כמו בקוד המקורי)
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # 3. יצירת שלד בסיסי (התוספת היחידה)
    # pda_skeleton = get_basic_skeleton(dark_pda_mask)
    
    # # שמירה
    # file_name = os.path.basename(image_path)
    # cv2.imwrite(os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}"), critical_roi_color)
    # cv2.imwrite(os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}"), dark_pda_mask)
    # cv2.imwrite(os.path.join(SKELETON_OUTPUT_DIR, f"skel_{file_name}"), pda_skeleton)

    # # 4. ויזואליזציה פשוטה
    # if debug:
        # print(f"--- Processing: {file_name} ---")
        # plt.figure(figsize=(12, 5))
        
        # plt.subplot(141)
        # plt.imshow(cv2.cvtColor(critical_roi_color, cv2.COLOR_BGR2RGB))
        # plt.title('Color ROI')
        
        # plt.subplot(142)
        # plt.imshow(critical_roi_gray, cmap='gray')
        # plt.title('Gray ROI')
        
        # plt.subplot(143)
        # plt.imshow(dark_pda_mask, cmap='gray')
        # plt.title('Basic Mask')
        
        # plt.subplot(144)
        # plt.imshow(pda_skeleton, cmap='gray')
        # plt.title('Basic Skeleton') # הנה השלד הגולמי
        
        # plt.tight_layout()
        # plt.show()

    # return True

# # --- רשימות הקבצים ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",      
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",       
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# if __name__ == "__main__":
    # print("--- בדיקת רכיבים פגומים (BASIC) ---")
    # for p in defective_images: analyze_pda_basic(p, debug=True)

    # print("\n--- בדיקת רכיבים תקינים (BASIC) ---")
    # for p in good_images: analyze_pda_basic(p, debug=True)



#####----------------------NOT GOOD !! - Mask and Skeletonization for PDA Defect Detection -------------------------------------#####


# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt

# # --- Parameters ---
# ROI_DIVISOR = 8 
# DARK_THRESHOLD = 35
# # סף מרחק: אם השפיץ האמיתי רחוק מהתיאורטי ביותר מ-X פיקסלים -> פגום
# # ברכיב תקין המרחק אמור להיות סביב 0-5. ברכיב שבור סביב 15-30.
# GAP_THRESHOLD = 10 

# SKELETON_OUTPUT_DIR = "output_skeleton_virtual_tip"
# if not os.path.exists(SKELETON_OUTPUT_DIR): os.makedirs(SKELETON_OUTPUT_DIR)

# def get_basic_skeleton(binary_img):
    # img = binary_img.copy()
    # skel = np.zeros(img.shape, np.uint8)
    # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    # while True:
        # open_op = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
        # temp = cv2.subtract(img, open_op)
        # eroded = cv2.erode(img, element)
        # skel = cv2.bitwise_or(skel, temp)
        # img = eroded.copy()
        # if cv2.countNonZero(img) == 0: break
    # return skel

# def find_intersection(line1, line2):
    # """ מוצא נקודת מפגש בין שני קווים """
    # vx1, vy1, x1, y1 = line1
    # vx2, vy2, x2, y2 = line2
    
    # # פתרון מערכת משוואות לינארית למציאת חיתוך
    # # Line 1: P1 = (x1, y1) + t1 * (vx1, vy1)
    # # Line 2: P2 = (x2, y2) + t2 * (vx2, vy2)
    # # אנחנו צריכים את נקודת החיתוך
    
    # # המרת לפורמט Ax + By = C
    # A1, B1 = -vy1, vx1
    # C1 = A1*x1 + B1*y1
    
    # A2, B2 = -vy2, vx2
    # C2 = A2*x2 + B2*y2
    
    # det = A1*B2 - A2*B1
    # if abs(det) < 1e-6: return None # קווים מקבילים
    
    # cx = (B2*C1 - B1*C2) / det
    # cy = (A1*C2 - A2*C1) / det
    
    # return int(cx), int(cy)

# def analyze_pda_virtual_tip(image_path, debug=False):
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    # x_end, y_end = x_start + roi_w, y_start + roi_h
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # # מסכה ושלד
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    # pda_skeleton = get_basic_skeleton(dark_pda_mask)
    
    # # --- NEW LOGIC: Fit Lines to Arms ---
    
    # # משיגים את כל הנקודות של השלד
    # points = cv2.findNonZero(pda_skeleton)
    # if points is None: return False
    # points = points[:, 0, :] # (x,y)
    
    # # ממיינים לפי Y (גובה)
    # points = points[points[:, 1].argsort()]
    
    # # לוקחים את ה-30% נקודות העליונות (זרוע עליונה)
    # num_pts = len(points)
    # top_arm_pts = points[:int(num_pts * 0.3)]
    # # לוקחים את ה-30% נקודות התחתונות (זרוע תחתונה)
    # bottom_arm_pts = points[int(num_pts * 0.7):]
    
    # if len(top_arm_pts) < 5 or len(bottom_arm_pts) < 5:
        # return False
    
    # # התאמת קו ישר לכל זרוע (Fit Line)
    # # מחזיר (vx, vy, x, y) - וקטור כיוון ונקודה על הקו
    # line_top = cv2.fitLine(top_arm_pts, cv2.DIST_L2, 0, 0.01, 0.01)
    # line_bottom = cv2.fitLine(bottom_arm_pts, cv2.DIST_L2, 0, 0.01, 0.01)
    
    # # מציאת נקודת החיתוך התיאורטית (איפה הפינה היתה צריכה להיות אם היא מושלמת)
    # virtual_tip = find_intersection(line_top, line_bottom)
    
    # if virtual_tip is None: return False
    # vx_tip, vy_tip = virtual_tip
    
    # # מציאת השפיץ האמיתי (הנקודה הכי שמאלית בשלד האמיתי)
    # # (תיקון קטן: נחפש את הנקודה הכי קרובה לנקודת המפגש התיאורטית)
    # distances = np.sqrt((points[:,0] - vx_tip)**2 + (points[:,1] - vy_tip)**2)
    # min_dist_idx = np.argmin(distances)
    # actual_tip = points[min_dist_idx]
    # gap_distance = distances[min_dist_idx]
    
    # is_defective = gap_distance > GAP_THRESHOLD
    
    # if debug:
        # file_name = os.path.basename(image_path)
        # print(f"--- {file_name} ---")
        # print(f"Gap Distance: {gap_distance:.2f} px (Threshold: {GAP_THRESHOLD})")
        
        # img_debug = cv2.cvtColor(critical_roi_gray, cv2.COLOR_GRAY2BGR)
        
        # # ציור הקווים התיאורטיים (כחול)
        # cv2.line(img_debug, (vx_tip, vy_tip), (int(line_top[2]), int(line_top[3])), (255, 0, 0), 1)
        # cv2.line(img_debug, (vx_tip, vy_tip), (int(line_bottom[2]), int(line_bottom[3])), (255, 0, 0), 1)
        
        # # ציור השלד (ירוק)
        # img_debug[pda_skeleton == 255] = [0, 255, 0]
        
        # # ציור השפיץ התיאורטי (איקס כחול)
        # cv2.drawMarker(img_debug, virtual_tip, (255, 0, 0), cv2.MARKER_CROSS, 10, 2)
        
        # # ציור השפיץ האמיתי (נקודה אדומה)
        # cv2.circle(img_debug, tuple(actual_tip), 4, (0, 0, 255), -1)
        
        # # קו המחבר ביניהם (הפער)
        # cv2.line(img_debug, virtual_tip, tuple(actual_tip), (0, 0, 255), 2)
        
        # plt.figure(figsize=(8, 6))
        # plt.imshow(cv2.cvtColor(img_debug, cv2.COLOR_BGR2RGB))
        # plt.title(f"Gap: {gap_distance:.1f}px\n{'DEFECTIVE' if is_defective else 'GOOD'}")
        # plt.show()
        
        # cv2.imwrite(os.path.join(SKELETON_OUTPUT_DIR, f"gap_{file_name}"), img_debug)

    # return not is_defective

# # --- רשימות הקבצים ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",      
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",       
# ]

# if __name__ == "__main__":
    # print("--- Checking Defective (Gap Analysis) ---")
    # for p in defective_images: analyze_pda_virtual_tip(p, debug=True)
    
    # print("\n--- Checking Good (Gap Analysis) ---")
    # for p in good_images: analyze_pda_virtual_tip(p, debug=True)


#####-------------------V7-----------------------------------------------------------########

# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt

# # --- Parameters ---
# ROI_DIVISOR = 8 
# DARK_THRESHOLD = 35

# # גודל הריבוע לבדיקה סביב השפיץ
# TIP_BOX_SIZE = 60 

# # סף Solidity (קמירות):
# # פינה תקינה היא קמורה וכמעט מלאה -> ערך קרוב ל-1.0 (למשל 0.95)
# # פינה שבורה היא "מכתש" -> הערך יורד (כי הגומייה מכסה שטח ריק)
# SOLIDITY_THRESHOLD = 0.88 

# OUTPUT_DIR = "output_v7_solidity"
# if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

# def analyze_pda_v7(image_path, debug=False):
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    # x_end, y_end = x_start + roi_w, y_start + roi_h
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # # 1. יצירת מסכה - ללא Dilation אגרסיבי!
    # _, mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # רק סגירה עדינה כדי למנוע רעש, אבל לא לנפח
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # mask_clean = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # # 2. מציאת השפיץ האמיתי (Leftmost Point)
    # contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if not contours: return False
    
    # # לוקחים את הקונטור הגדול ביותר (ה-PDA)
    # c = max(contours, key=cv2.contourArea)
    
    # # מוצאים את הנקודה הכי שמאלית בקונטור (ללא תלות בפינות)
    # # זה מבטיח שהריבוע יהיה על הקצה, גם אם הוא שבור
    # extLeft = tuple(c[c[:, :, 0].argmin()][0])
    # tip_x, tip_y = extLeft
    
    # # 3. גזירת ROI סביב השפיץ
    # box_half = TIP_BOX_SIZE // 2
    # x1 = max(0, tip_x - 10) # מתחילים קצת לפני השפיץ
    # y1 = max(0, tip_y - box_half)
    # x2 = min(W, tip_x + TIP_BOX_SIZE)
    # y2 = min(H, tip_y + box_half)
    
    # tip_roi_mask = mask_clean[y1:y2, x1:x2]
    
    # # 4. חישוב Solidity בתוך הריבוע הקטן
    # # אנחנו בודקים את הצורה של הפינה בלבד
    # tip_contours, _ = cv2.findContours(tip_roi_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # if not tip_contours:
        # solidity = 0
    # else:
        # largest_tip_c = max(tip_contours, key=cv2.contourArea)
        # area = cv2.contourArea(largest_tip_c)
        # hull = cv2.convexHull(largest_tip_c)
        # hull_area = cv2.contourArea(hull)
        
        # if hull_area > 0:
            # solidity = area / hull_area
        # else:
            # solidity = 0

    # # החלטה: שבר יוצר "מפרץ" או שקע -> שטח הקונטור קטן משטח ה-Hull -> Solidity נמוך
    # is_defective = solidity < SOLIDITY_THRESHOLD
    
    # if debug:
        # file_name = os.path.basename(image_path)
        # print(f"--- {file_name} ---")
        # print(f"Solidity: {solidity:.3f} (Threshold: {SOLIDITY_THRESHOLD})")
        
        # img_debug = cv2.cvtColor(critical_roi_gray, cv2.COLOR_GRAY2BGR)
        
        # # ציור הריבוע והשפיץ
        # cv2.rectangle(img_debug, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # cv2.circle(img_debug, extLeft, 5, (0, 0, 255), -1)
        
        # # ציור ה-Hull בתוך הריבוע (להמחשה)
        # # זה מצריך קצת אקרובטיקה לציור על התמונה המקורית, נעשה את זה פשוט בחלון נפרד
        
        # plt.figure(figsize=(10, 4))
        # plt.subplot(131), plt.imshow(mask_clean, cmap='gray'), plt.title("Clean Mask (No Dilation)")
        
        # # תצוגת הזום עם ה-Hull
        # debug_roi = cv2.cvtColor(tip_roi_mask, cv2.COLOR_GRAY2BGR)
        # if tip_contours:
            # cv2.drawContours(debug_roi, [largest_tip_c], -1, (0, 255, 0), 1) # ירוק = צורה אמיתית
            # cv2.drawContours(debug_roi, [hull], -1, (0, 0, 255), 1)      # אדום = גומייה (Hull)
            
        # plt.subplot(132), plt.imshow(debug_roi), plt.title(f"Tip Analysis\nGreen=Obj, Red=Hull")
        
        # plt.subplot(133), plt.imshow(cv2.cvtColor(img_debug, cv2.COLOR_BGR2RGB))
        # plt.title(f"Solidity: {solidity:.2f}\n{'DEFECTIVE' if is_defective else 'GOOD'}")
        # plt.tight_layout()
        # plt.show()
        
        # cv2.imwrite(os.path.join(OUTPUT_DIR, f"v7_{file_name}"), img_debug)

    # return not is_defective

# # --- הרצה ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",      
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",       
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# if __name__ == "__main__":
    # print("--- Checking Defective (V7 Solidity) ---")
    # for p in defective_images: analyze_pda_v7(p, debug=True)
    
    # print("\n--- Checking Good (V7 Solidity) ---")
    # for p in good_images: analyze_pda_v7(p, debug=True)



####--------------------V7b------------------------------------------------------------------------------##############

# import cv2
# import numpy as np
# import os
# from matplotlib import pyplot as plt

# # --- Parameters ---
# ROI_DIVISOR = 8 
# DARK_THRESHOLD = 40  # סף רגישות לחומר

# # גודל הריבוע לבדיקה סביב הפינה
# TIP_BOX_SIZE = 70 

# # סף החלטה (Solidity):
# # רכיב תקין יהיה מעל 0.90 (כמעט מושלם)
# # רכיב שבור יהיה מתחת (בגלל השקע)
# SOLIDITY_THRESHOLD = 0.89

# OUTPUT_DIR = "output_v7_refined"
# if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

# def analyze_pda_v7_refined(image_path, debug=False):
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    
    # # 1. חיתוך ROI (כמו תמיד)
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    # x_end, y_end = x_start + roi_w, y_start + roi_h
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # # 2. יצירת מסכה "כנה" (ללא ניפוח מזויף)
    # # משתמשים ב-Morphological Close כדי לסתום רעשים פנימיים בלבד
    # _, mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    # mask_clean = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    # # ניקוי רעשים זעירים (נקודות בודדות)
    # mask_clean = cv2.morphologyEx(mask_clean, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))

    # # 3. מציאת הפינה (הנקודה הכי שמאלית בקונטור הראשי)
    # contours, _ = cv2.findContours(mask_clean, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if not contours: 
        # print(f"Skipping {os.path.basename(image_path)}: No contour")
        # return False
    
    # # לוקחים את הגוף הגדול ביותר (ה-PDA)
    # c = max(contours, key=cv2.contourArea)
    
    # # מוצאים את הנקודה עם ה-X הכי נמוך (הכי שמאלה)
    # extLeft = tuple(c[c[:, :, 0].argmin()][0])
    # tip_x, tip_y = extLeft
    
    # # 4. יצירת ריבוע הבדיקה (Local ROI)
    # box_half = TIP_BOX_SIZE // 2
    # x1 = max(0, tip_x - 10) # מתחילים קצת לפני השפיץ
    # y1 = max(0, tip_y - box_half)
    # x2 = min(W, tip_x + TIP_BOX_SIZE)
    # y2 = min(H, tip_y + box_half)
    
    # # גוזרים את המסכה באזור הזה בלבד
    # local_mask = mask_clean[y1:y2, x1:x2]
    
    # # 5. חישוב Solidity בתוך הריבוע
    # local_contours, _ = cv2.findContours(local_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # solidity = 0.0
    # hull_draw = None
    # contour_draw = None
    
    # if local_contours:
        # # לוקחים את הקונטור הכי גדול בתוך הריבוע הקטן
        # largest_local_c = max(local_contours, key=cv2.contourArea)
        # area = cv2.contourArea(largest_local_c)
        
        # # חישוב הקמירות (Convex Hull)
        # hull = cv2.convexHull(largest_local_c)
        # hull_area = cv2.contourArea(hull)
        
        # if hull_area > 0:
            # solidity = area / hull_area
            # hull_draw = hull
            # contour_draw = largest_local_c

    # # 6. החלטה
    # is_defective = solidity < SOLIDITY_THRESHOLD
    
    # # --- Debug Visualization ---
    # if debug:
        # file_name = os.path.basename(image_path)
        # print(f"--- {file_name} ---")
        # print(f"Solidity: {solidity:.3f} (Threshold: {SOLIDITY_THRESHOLD})")
        
        # img_debug = cv2.cvtColor(critical_roi_gray, cv2.COLOR_GRAY2BGR)
        
        # # ציור הריבוע הכחול
        # cv2.rectangle(img_debug, (x1, y1), (x2, y2), (255, 0, 0), 2)
        # # ציור נקודת השפיץ
        # cv2.circle(img_debug, extLeft, 4, (0, 0, 255), -1)
        
        # # הכנת תמונת זום להצגת ה-Hull
        # zoom_view = cv2.cvtColor(local_mask, cv2.COLOR_GRAY2BGR)
        # if contour_draw is not None and hull_draw is not None:
            # # ירוק = הצורה המקורית
            # cv2.drawContours(zoom_view, [contour_draw], -1, (0, 255, 0), 2)
            # # אדום = הגומייה (ההשלמה)
            # cv2.drawContours(zoom_view, [hull_draw], -1, (0, 0, 255), 2)
            
        # plt.figure(figsize=(12, 4))
        
        # # תצוגה 1: המסכה הנקייה (לוודא שאין חורים סתומים)
        # plt.subplot(131)
        # plt.imshow(mask_clean, cmap='gray')
        # plt.title("Clean Mask (No Dilation)")
        
        # # תצוגה 2: זום על הפינה (הבדיקה האמיתית)
        # plt.subplot(132)
        # plt.imshow(cv2.cvtColor(zoom_view, cv2.COLOR_BGR2RGB))
        # plt.title(f"Green=Obj, Red=Hull\nSolidity: {solidity:.3f}")
        
        # # תצוגה 3: התוצאה הסופית על התמונה
        # plt.subplot(133)
        # plt.imshow(cv2.cvtColor(img_debug, cv2.COLOR_BGR2RGB))
        # plt.title(f"Result: {'❌ DEFECTIVE' if is_defective else '✅ GOOD'}")
        
        # plt.tight_layout()
        # plt.show()
        
        # cv2.imwrite(os.path.join(OUTPUT_DIR, f"v7_refined_{file_name}"), img_debug)

    # return not is_defective

# # --- הרצה ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",      
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",       
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# if __name__ == "__main__":
    # print("--- V7 Refined (Solidity) Check ---")
    # print("Checking Defective:")
    # for p in defective_images: analyze_pda_v7_refined(p, debug=True)
    # print("\nChecking Good:")
    # for p in good_images: analyze_pda_v7_refined(p, debug=True)



######--------------------The Virtual Corner----------------------------------------------------####

# import cv2
# import numpy as np
# import os

# # --- Constants ---
# DARK_THRESHOLD = 35
# ROI_DIVISOR = 8 

# # --- הגדרת "מלכודת" (Trap) ---
# # גודל הריבוע שנבדוק (בפיקסלים)
# TRAP_SIZE = 20 
# # סף פיקסלים: אם יש פחות מ-X% פיקסלים לבנים בריבוע, זה פגום.
# # נתחיל ב-20% (שזה 0.2 * 20*20 = 80 פיקסלים)
# PIXEL_COUNT_THRESHOLD = (TRAP_SIZE * TRAP_SIZE) * 0.20

# # --- Paths ---
# OUTPUT_DIR = "output_trap_check"
# if not os.path.exists(OUTPUT_DIR):
    # os.makedirs(OUTPUT_DIR)

# def analyze_pda_trap_density(image_path, debug=False):
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # # 1. עיבוד ראשוני (סטנדרטי)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    
    # critical_roi_gray = gray[y_start:y_start+roi_h, x_start:x_start+roi_w]
    # critical_roi_color = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
    # kernel = np.ones((3, 3), np.uint8)
    # mask = cv2.morphologyEx(dark_pda_mask, cv2.MORPH_OPEN, kernel)
    # mask_final = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # # 2. מציאת הקונטור (כדי לדעת איפה למקם את המלכודת)
    # contours, _ = cv2.findContours(mask_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # if not contours: return False
    # c = max(contours, key=cv2.contourArea)
    
    # # נמצא את הנקודה הכי נמוכה (הכי גדולה ב-Y) בקונטור
    # # זה יעזור לנו למקם את הריבוע באזור הכללי הנכון גם אם הרכיב זז קצת
    # bottom_most_point = tuple(c[c[:, :, 1].argmax()][0])
    # bx, by = bottom_most_point

    # # 3. הגדרת אזור המלכודת (Trap Region)
    # # נמקם את הריבוע כך שהנקודה הכי נמוכה שמצאנו תהיה במרכזו (בערך)
    # trap_x1 = max(0, bx - TRAP_SIZE // 2)
    # trap_y1 = max(0, by - TRAP_SIZE // 2)
    # trap_x2 = min(roi_w, trap_x1 + TRAP_SIZE)
    # trap_y2 = min(roi_h, trap_y1 + TRAP_SIZE)
    
    # # חילוץ אזור המלכודת מתוך המסכה
    # trap_roi = mask_final[trap_y1:trap_y2, trap_x1:trap_x2]
    
    # # 4. ספירת פיקסלים לבנים (הבדיקה עצמה)
    # white_pixels = cv2.countNonZero(trap_roi)
    
    # # 5. קבלת החלטה
    # # ברכיב תקין, הריבוע הזה אמור להיות מלא חלקית בחומר.
    # # ברכיב שבור, הנקודה הכי נמוכה היא כבר חלק מהשבר, ולכן הריבוע סביבה יכיל פחות חומר.
    # is_good = white_pixels > PIXEL_COUNT_THRESHOLD

    # # --- Debug ---
    # if debug:
        # debug_img = critical_roi_color.copy()
        
        # # ציור הריבוע על תמונת הדיבאג (צהוב)
        # cv2.rectangle(debug_img, (trap_x1, trap_y1), (trap_x2, trap_y2), (0, 255, 255), 2)
        
        # status = "GOOD" if is_good else "DEFECT"
        # color = (0, 255, 0) if is_good else (0, 0, 255)
        
        # # הצגת כמות הפיקסלים שנמצאה
        # label = f"Px Count: {white_pixels} (Thresh: {int(PIXEL_COUNT_THRESHOLD)}) | {status}"
        # cv2.putText(debug_img, label, (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)
        
        # cv2.imwrite(os.path.join(OUTPUT_DIR, f"trap_{os.path.basename(image_path)}"), debug_img)
        # print(f"File: {os.path.basename(image_path)} | White Pixels: {white_pixels} | Status: {status}")

    # return is_good

# # --- Run List ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",      
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# if __name__ == "__main__":
    # print(f"Trap Size: {TRAP_SIZE}x{TRAP_SIZE}, Threshold: {PIXEL_COUNT_THRESHOLD} pixels")
    # print("\n--- Checking Defective (Expect LOW Pixel Count) ---")
    # for img in defective_images: analyze_pda_trap_density(img, debug=True)
    
    # print("\n--- Checking Good (Expect HIGH Pixel Count) ---")
    # for img in good_images: analyze_pda_trap_density(img, debug=True)
    
    
########------------------------Skeleton Continuity -------------------------------------###############


# import cv2
# import numpy as np
# import os

# # --- Tuned global parameters ---
# FINAL_VARIANCE_THRESHOLD = 42
# DARK_THRESHOLD = 35
# ROI_DIVISOR = 8 

# # --- NEW: פרמטרים לבדיקת השלד ---
# MIN_SKELETON_LENGTH = 30  # אורך מינימלי (בפיקסלים) כדי שחלק ייחשב "חתיכה אמיתית"
# MAX_ALLOWED_COMPONENTS = 1 # כמה חתיכות שלד מותר שיהיו (1 = רציף, >1 = שבור)

# # הגדרת נתיבי תיקיות לשמירה
# ROI_OUTPUT_DIR = "output_roi"
# MASK_OUTPUT_DIR = "output_mask"
# SKEL_OUTPUT_DIR = "output_skeleton" # תוספת לשמירת תמונת השלד

# # יצירת התיקיות
# for path in [ROI_OUTPUT_DIR, MASK_OUTPUT_DIR, SKEL_OUTPUT_DIR]:
    # if not os.path.exists(path):
        # os.makedirs(path)

# ## --- NEW: פונקציית עזר ליצירת שלד --- ##
# def get_gentle_skeleton(mask):
    # """
    # יוצרת שלד (Skeleton) מהמסכה הבינארית.
    # משתמשת בשיטת שחיקה (Erosion) פשוטה שנתמכת בכל גרסאות OpenCV.
    # """
    # skel = np.zeros(mask.shape, np.uint8)
    # img = mask.copy()
    # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    
    # while True:
        # eroded = cv2.erode(img, element)
        # temp = cv2.dilate(eroded, element)
        # temp = cv2.subtract(img, temp)
        # skel = cv2.bitwise_or(skel, temp)
        # img = eroded.copy()
        
        # # אם לא נשארו פיקסלים לבנים, סיימנו
        # if cv2.countNonZero(img) == 0:
            # break
            
    # return skel
# ## ------------------------------------ ##

# def analyze_pda_integrity_final_optimized(image_path, debug=False):
    # # 1. Load image
    # img = cv2.imread(image_path)
    # if img is None:
        # return False
        
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    
    # # 2. Compute ROI
    # roi_w = max(1, W // ROI_DIVISOR)
    # roi_h = max(1, H // ROI_DIVISOR)
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    # x_end = x_start + roi_w
    # y_end = y_start + roi_h
    
    # critical_roi_gray = gray[y_start:y_end, x_start:x_end].copy()
    
    # if critical_roi_gray.size == 0:
        # return False
        
    # # 3. Create Mask
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # ניקוי וסגירה (כמו בקוד המקורי שלך)
    # kernel = np.ones((3, 3), np.uint8) 
    # mask_cleaned = cv2.morphologyEx(dark_pda_mask, cv2.MORPH_OPEN, kernel)
    # mask_final = cv2.morphologyEx(mask_cleaned, cv2.MORPH_CLOSE, kernel)

    # # --- שמירת קבצים ---
    # file_name = os.path.basename(image_path)
    # cv2.imwrite(os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}"), img[y_start:y_end, x_start:x_end])
    # cv2.imwrite(os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}"), mask_final)

    # # -----------------------------------------------------------
    # # --- NEW: בדיקת רציפות שלד (Skeleton Continuity) ---
    # # -----------------------------------------------------------
    
    # # 1. יצירת השלד מהמסכה הנקייה
    # skeleton = get_gentle_skeleton(mask_final)
    
    # # 2. מציאת רכיבים (Contours) בתוך השלד
    # contours, _ = cv2.findContours(skeleton, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # # 3. סינון עדין: סופרים רק חתיכות שלד משמעותיות
    # # (מתעלמים מ"לכלוך" קטן של כמה פיקסלים)
    # valid_skeleton_parts = 0
    # for cnt in contours:
        # # בודקים אורך הקו (Arc Length)
        # length = cv2.arcLength(cnt, False) # False כי השלד לא סגור
        # if length > MIN_SKELETON_LENGTH:
            # valid_skeleton_parts += 1
            
    # # שמירת תמונת השלד לבדיקה ויזואלית
    # cv2.imwrite(os.path.join(SKEL_OUTPUT_DIR, f"skel_{file_name}"), skeleton)

    # # החלטה האם השלד שבור
    # is_skeleton_broken = valid_skeleton_parts > MAX_ALLOWED_COMPONENTS
    
    # if debug:
        # print(f"   [Skeleton Analysis] Found {valid_skeleton_parts} valid parts. (Broken? {is_skeleton_broken})")

    # # -----------------------------------------------------------
    # # --- סוף חלק חדש ---
    # # -----------------------------------------------------------

    # # 4. Variance analysis (הקוד המקורי שלך)
    # pda_pixels = critical_roi_gray[mask_final == 255]
    
    # if pda_pixels.size < 50: 
          # variance = 5000 
    # else:
        # variance = np.var(pda_pixels)
    
    # is_variance_high = variance > FINAL_VARIANCE_THRESHOLD

    # # 5. Final decision: פסול אם ה-Variance גבוה או אם השלד שבור
    # is_defective = is_variance_high or is_skeleton_broken

    # # Return True if component is GOOD     
    # return not is_defective

# # --- רשימות התמונות שלך (אותן רשימות כמו בקוד המקורי) ---
# # ... (ניתן להעתיק את רשימות defective_images ו-good_images מהקוד שלך)
# # --- Run List ---
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",     
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",     
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",          
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"            
# ]

# # --- הרצה ---
# if __name__ == "__main__":
    
    # # ודא שהפונקציה analyze_pda_integrity_final_optimized מוגדרת וזמינה
    
    # print("--- בדיקת רכיבים פגומים (צפוי: ❌ DEFECTIVE) ---")
    # for img_path in defective_images:
        
        # # 🟢 התיקון: שימוש ישיר בנתיב ה-.PNG שסופק
        # path_to_use = img_path 
        
        # # אם התמונות שלך הן באמת JPG, הסר את כל ה-.PNG מהרשימה
        # # אם הן PNG, התיקון הזה עובד.

        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"{os.path.basename(path_to_use)}: {status}")

    # print("\n--- בדיקת רכיבים תקינים (צפוי: ✅ GOOD) ---")
    # for img_path in good_images:
        
        # # 🟢 התיקון: שימוש ישיר בנתיב ה-.PNG שסופק
        # path_to_use = img_path
        
        # is_good = analyze_pda_integrity_final_optimized(path_to_use, debug=True)
        # status = "✅ GOOD" if is_good else "❌ DEFECTIVE"
        # print(f"{os.path.basename(path_to_use)}: {status}")


#########-------------------------------------------------------------------------------#####

# import cv2
# import numpy as np
# import os

# # --- Tuned global parameters ---
# FINAL_VARIANCE_THRESHOLD = 42
# DARK_THRESHOLD = 35
# ROI_DIVISOR = 8 

# # --- NEW: פרמטרים לחיבור השלד השבור ---
# SKELETON_CONNECT_DIST = 5   # קריטי: מרחק בפיקסלים שבו "מקפים" יחוברו לקו אחד
# MIN_SKELETON_LENGTH = 40    # סינון רעשים קטנים (הגדלנו קצת)
# MAX_ALLOWED_COMPONENTS = 1  # שואפים לרכיב אחד רציף

# # נתיבים לשמירה
# ROI_OUTPUT_DIR = "output_roi"
# MASK_OUTPUT_DIR = "output_mask"
# SKEL_OUTPUT_DIR = "output_skeleton"

# # יצירת תיקיות
# for path in [ROI_OUTPUT_DIR, MASK_OUTPUT_DIR, SKEL_OUTPUT_DIR]:
    # if not os.path.exists(path):
        # os.makedirs(path)

# ## --- פונקציית שלד (ללא שינוי) --- ##
# def get_gentle_skeleton(mask):
    # skel = np.zeros(mask.shape, np.uint8)
    # img = mask.copy()
    # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    
    # while True:
        # eroded = cv2.erode(img, element)
        # temp = cv2.dilate(eroded, element)
        # temp = cv2.subtract(img, temp)
        # skel = cv2.bitwise_or(skel, temp)
        # img = eroded.copy()
        
        # if cv2.countNonZero(img) == 0:
            # break
            
    # return skel
# ## ------------------------------------ ##

# def analyze_pda_integrity_final_optimized(image_path, debug=False):
    # # 1. Load image
    # img = cv2.imread(image_path)
    # if img is None: return False
    
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # H, W = gray.shape
    
    # # 2. Compute ROI
    # roi_w, roi_h = max(1, W // ROI_DIVISOR), max(1, H // ROI_DIVISOR)
    # x_start, y_start = (W - roi_w) // 2, (H - roi_h) // 2
    # critical_roi_gray = gray[y_start:y_start + roi_h, x_start:x_start + roi_w].copy()
    
    # if critical_roi_gray.size == 0: return False
        
    # # 3. Create Mask
    # _, dark_pda_mask = cv2.threshold(critical_roi_gray, DARK_THRESHOLD, 255, cv2.THRESH_BINARY_INV) 
    
    # # --- תיקון 1: סגירה אגרסיבית יותר על המסכה המקורית ---
    # # זה נועד למנוע חורים בתוך הבלוק השחור עוד לפני שהופכים אותו לקו
    # kernel_mask = np.ones((5, 5), np.uint8) 
    # mask_closed = cv2.morphologyEx(dark_pda_mask, cv2.MORPH_CLOSE, kernel_mask)
    
    # # שמירת קבצים
    # file_name = os.path.basename(image_path)
    # cv2.imwrite(os.path.join(ROI_OUTPUT_DIR, f"roi_{file_name}"), img[y_start:y_start+roi_h, x_start:x_start+roi_w])
    # cv2.imwrite(os.path.join(MASK_OUTPUT_DIR, f"mask_{file_name}"), mask_closed)

    # # -----------------------------------------------------------
    # # --- בדיקת רציפות שלד (Skeleton Analysis) ---
    # # -----------------------------------------------------------
    
    # # 1. יצירת השלד
    # skeleton = get_gentle_skeleton(mask_closed)
    
    # # --- תיקון 2: חיבור נקודות (Connecting the Dots) ---
    # # הפעולה הזו מחברת את הקווים המקווקוים לקו אחד רציף
    # # אם השבר אמיתי (Crack), הרווח יהיה גדול יותר מ-Kernel ולכן לא יתחבר.
    # connect_kernel = np.ones((SKELETON_CONNECT_DIST, SKELETON_CONNECT_DIST), np.uint8)
    # skeleton_connected = cv2.morphologyEx(skeleton, cv2.MORPH_CLOSE, connect_kernel)
    
    # # 2. מציאת רכיבים בשלד המחובר
    # contours, _ = cv2.findContours(skeleton_connected, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # # 3. ספירה חכמה: רק חלקים משמעותיים
    # valid_skeleton_parts = 0
    
    # # נשמור תמונה ויזואלית של מה שהמחשב "רואה" כחלקים
    # debug_skel_color = cv2.cvtColor(skeleton_connected, cv2.COLOR_GRAY2BGR)

    # for cnt in contours:
        # length = cv2.arcLength(cnt, False) # False כי הקו פתוח
        
        # if length > MIN_SKELETON_LENGTH:
            # valid_skeleton_parts += 1
            # # צובעים בירוק חלקים שנחשבים תקינים/גדולים
            # cv2.drawContours(debug_skel_color, [cnt], -1, (0, 255, 0), 1)
        # else:
            # # צובעים באדום רעש
            # cv2.drawContours(debug_skel_color, [cnt], -1, (0, 0, 255), 1)
            
    # # שמירת השלד ה"מחובר" לבדיקה
    # cv2.imwrite(os.path.join(SKEL_OUTPUT_DIR, f"skel_connected_{file_name}"), debug_skel_color)

    # # החלטה: אם יש יותר מרכיב משמעותי אחד -> זה שבור
    # is_skeleton_broken = valid_skeleton_parts > MAX_ALLOWED_COMPONENTS
    
    # if debug:
        # print(f"   [Skeleton] Parts: {valid_skeleton_parts} (Broken: {is_skeleton_broken}) -> Saved skel_connected_{file_name}")

    # # 4. Variance analysis (כרגיל)
    # pda_pixels = critical_roi_gray[mask_closed == 255]
    # variance = np.var(pda_pixels) if pda_pixels.size >= 50 else 5000
    # is_variance_high = variance > FINAL_VARIANCE_THRESHOLD

    # # 5. Final decision
    # is_defective = is_variance_high or is_skeleton_broken

    # return not is_defective

# # --- הרצה ---
# # (אותו חלק Main כמו אצלך)
# defective_images = [
    # "/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/32_0331_3th_corner_2.PNG",
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_broken_2th_corner_4.PNG", 
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_broken_4th_corner.PNG",   
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/32_0331/32_0331_4th_corner_5.PNG",     
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/30_1493/30_1493_2th_corner_7.PNG",     
# ]

# good_images = [
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_1th_corner.PNG",           
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/28_0615/28_0615_3th_corner.PNG",      
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/114/114_4th_corner_3.PNG",            
    # "/home/pda-chipping/HQ_Camera_Codes_and_Pics/113/113_2th_corner.PNG"              
# ]

# if __name__ == "__main__":
    # print("--- Testing Optimized Skeleton Logic ---")
    
    # print("\n--- Expected: FAIL (Defective) ---")
    # for img_path in defective_images:
        # is_good = analyze_pda_integrity_final_optimized(img_path, debug=True)
        # print(f"{os.path.basename(img_path)}: {'✅ GOOD' if is_good else '❌ DEFECTIVE'}")

    # print("\n--- Expected: PASS (Good) ---")
    # for img_path in good_images:
        # is_good = analyze_pda_integrity_final_optimized(img_path, debug=True)
        # print(f"{os.path.basename(img_path)}: {'✅ GOOD' if is_good else '❌ DEFECTIVE'}")
