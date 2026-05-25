# import cv2
# import numpy as np

# # Read image
# im = cv2.imread('/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/ROI_Output/111_4th_corner_broken_ROI4.PNG')

# # Convert BGR to HSV
# hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# # Define yellow range (experiment with values!)
# h_low, h_high = 15, 37   # Hue range for yellow
# s_low, s_high = 60, 199  # Saturation range
# v_low, v_high = 120, 199  # Value range

# # Create binary mask
# bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

# # Morphological cleanup:
# kernel = np.ones((7,7), np.uint8)
# opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)   # מסיר נקודות קטנות
# cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)  # ממלא חורים קטנים


 # # =========================================================================
# #  חלק חדש: סינון גיאומטרי להסרת קווים
# # =========================================================================

# # 1. יצירת מסכה נקייה חדשה (שחורה לגמרי בהתחלה)
# final_mask = np.zeros_like(cleaned)

# # 2. מציאת כל הכתמים (Contours) במסכה הקיימת
# contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
    # # חישוב שטח כדי לסנן רעשים קטנים מאוד
    # area = cv2.contourArea(cnt)
    # if area < 50: # סף מינימלי לרעש, אפשר לשחק עם זה
        # continue

    # # שימוש ב-minAreaRect כדי לקבל מלבן חוסם מינימלי (שיודע להסתובב באלכסון)
    # # זה קריטי כי הקו שלך הוא אלכסוני!
    # rect = cv2.minAreaRect(cnt)
    # (center), (width, height), angle = rect

    # # חישוב יחס האורך-רוחב (Aspect Ratio)
    # # אנו רוצים לוודא שאנחנו לא מחלקים ב-0
    # if width == 0 or height == 0:
        # continue
    
    # # מסדרים ש-long_side יהיה הצלע הארוכה ו-short_side הקצרה
    # long_side = max(width, height)
    # short_side = min(width, height)
    
    # aspect_ratio = long_side / short_side

    # # === התנאי החשוב ===
    # # קו הוא אובייקט שהאורך שלו גדול משמעותית מהרוחב שלו.
    # # אם היחס גדול מ-4 (למשל), זה כנראה קו ולא שבר.
    # # השבר הוא לרוב יותר "עגול" או "מרובע".
    # if aspect_ratio < 2.0: 
        # # אם זה לא קו ארוך -> צייר אותו על המסכה החדשה
        # cv2.drawContours(final_mask, [cnt], -1, 255, thickness=cv2.FILLED)
    # else:
        # print(f"Filtered out a line with Aspect Ratio: {aspect_ratio:.2f}")

# # מעדכנים את המשתנה cleaned להיות המסכה המסוננת
# cleaned = final_mask

# ###-------------------------------####

# # ---------- ספירת פיקסלים לבנים ----------
# white_pixels = cv2.countNonZero(cleaned)
# print("Number of white pixels in mask:", white_pixels)

# # אחוזים מתוך כל התמונה
# total_pixels = cleaned.size
# percent_white = (white_pixels / total_pixels) * 100
# print("White area percentage:", percent_white, "%")

# # Resize for display
# display_width = 600
# h_img, w_img = im.shape[:2]
# scale = display_width / w_img
# display_height = int(h_img * scale)

# im_small = cv2.resize(im, (display_width, display_height), interpolation=cv2.INTER_AREA)
# cleaned_small = cv2.resize(cleaned, (display_width, display_height), interpolation=cv2.INTER_NEAREST)

# cleaned_color = cv2.cvtColor(cleaned_small, cv2.COLOR_GRAY2BGR)
# combined = np.hstack((im_small, cleaned_color))

# # ---------- פונקציה לבדיקת ערכים בלחיצה ----------
# def pick_color(event, x, y, flags, param):
    # if event == cv2.EVENT_LBUTTONDOWN:
        # # לחיצה על החצי השמאלי בלבד (התמונה המקורית)
        # if x < display_width:
            # scale_x = w_img / display_width
            # scale_y = h_img / display_height
            # orig_x = int(x * scale_x)
            # orig_y = int(y * scale_y)

            # pixel = hsv[orig_y, orig_x]
            # print(f"Pixel at ({orig_x},{orig_y}) -> H:{pixel[0]} S:{pixel[1]} V:{pixel[2]}")
        # else:
            # print("לחצת על המסכה, אין ערכי HSV מקוריים שם.")

# # יצירת חלון והוספת callback
# cv2.namedWindow("Original (left) + Mask (right)")
# cv2.setMouseCallback("Original (left) + Mask (right)", pick_color)

# cv2.imshow("Original (left) + Mask (right)", combined)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


####--------------------------------VANISH WHITE LINE AND DOTS AND GIVE FINAL CLASS----------------------------------------------------------####

import cv2
import numpy as np

# ==========================================
# הגדרות ופרמטרים (כאן משנים ערכים)
# ==========================================
# נתיב לתמונה
IMAGE_PATH = '/home/pda-chipping/Codes - Final/Test_Results/SN_10_02_26_14:07/corner_4_10_02_26_14:07_ROI.PNG'

# ערכי HSV לצהוב
h_low, h_high = 4, 37 #15,37
s_low, s_high = 60, 200 #60, 199
v_low, v_high = 90,200 #90, 200

# פרמטרים לסינון רעשים
MIN_AREA_THRESHOLD = 100#300   # כתמים קטנים מזה יימחקו (רעש)
MAX_ASPECT_RATIO = 3.8 #3.8 #3.8    # צורות "ארוכות" יותר מהיחס הזה יימחקו (פסים/קווים) #5
MORPH_KERNEL_SIZE = (5, 5) # גודל המסנן הראשוני (מספר אי-זוגי)

# ==========================================

# קריאת התמונה
im = cv2.imread(IMAGE_PATH)
if im is None:
    print(f"Error: Could not load image from {IMAGE_PATH}")
    exit()

# המרה ל-HSV
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# יצירת מסכה בינארית ראשונית
bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

# ==========================================
# תוספת: מחיקת רעשים בצד ימין (20% מהתמונה)
# ==========================================
h, w = bw.shape[:2]       # בדיקת הגודל של התמונה
cutoff_x = int(w * 0.85)   # חישוב הנקודה שבה מתחיל ה-20% הימני
bw[:, cutoff_x:] = 0      # איפוס (השחרה) של כל האזור הימני הזה
# ==========================================

# ניקוי מורפולוגי (OPEN מנקה נקודות לבנות, CLOSE סוגר חורים שחורים)
kernel = np.ones(MORPH_KERNEL_SIZE, np.uint8)
opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

# =========================================================================
#  חלק הסינון המתקדם: גיאומטריה ושטח
# =========================================================================

# יצירת מסכה סופית ריקה (שחורה)
final_mask = np.zeros_like(cleaned)

# מציאת קונטורים (כתמים)
contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(f"--- Processing {len(contours)} potential objects ---")

for i, cnt in enumerate(contours):
    # 1. בדיקת שטח (Area)
    area = cv2.contourArea(cnt)
    
    if area < MIN_AREA_THRESHOLD:
        # אם הכתם קטן מדי -> דלג עליו
        # print(f"Object {i}: Rejected (Too small: {area})")
        continue

    # 2. בדיקת יחס אורך/רוחב (Aspect Ratio) עבור קווים
    rect = cv2.minAreaRect(cnt)
    (center), (w, h), angle = rect
    
    # מניעת חלוקה באפס
    if w == 0 or h == 0:
        continue
        
    # חישוב היחס (תמיד הגדול לחלק לקטן)
    aspect_ratio = max(w, h) / min(w, h)

    if aspect_ratio < MAX_ASPECT_RATIO:
        # עבר את כל הסינונים! זה השבר האמיתי -> צייר אותו על המסכה הסופית
        print(f"Object {i}: KKEPT (Area: {area:.1f}, Aspect Ratio: {aspect_ratio:.2f})")
        cv2.drawContours(final_mask, [cnt], -1, 255, thickness=cv2.FILLED)
    else:
        # נפל בסינון גיאומטרי (זה כנראה קו/השתקפות)
        print(f"Object {i}: Rejected (Looks like a line, AR: {aspect_ratio:.2f})")

# מעדכנים את המשתנה cleaned לתוצאה הסופית
cleaned = final_mask

# =========================================================================
#  חישובים ותצוגה
# =========================================================================

# ספירת פיקסלים לבנים
white_pixels = cv2.countNonZero(cleaned)
print("-" * 30)
print("Final white pixels count:", white_pixels)

# אחוזים
total_pixels = cleaned.size
percent_white = (white_pixels / total_pixels) * 100
print(f"White area percentage: {percent_white:.4f}%")

# שינוי גודל לתצוגה נוחה במסך
display_width = 800
h_img, w_img = im.shape[:2]
scale = display_width / w_img
display_height = int(h_img * scale)

im_small = cv2.resize(im, (display_width, display_height), interpolation=cv2.INTER_AREA)
cleaned_small = cv2.resize(cleaned, (display_width, display_height), interpolation=cv2.INTER_NEAREST)

# המרת המסכה לצבע כדי לחבר לתמונה המקורית
cleaned_color = cv2.cvtColor(cleaned_small, cv2.COLOR_GRAY2BGR)

# הדגשת האזור שנמצא על התמונה המקורית (אופציונלי - מוסיף קונטור ירוק על המקור)
contours_small, _ = cv2.findContours(cleaned_small, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(im_small, contours_small, -1, (0, 255, 0), 2)

# חיבור התמונות
combined = np.hstack((im_small, cleaned_color))

# ---------------------------------------------------------
# חלק חדש: בדיקת תקינות (PASS/FAIL)
# ---------------------------------------------------------

# הגדרת הסף (כפי שביקשת - 1200)
FAIL_THRESHOLD = 1200 #1200 

# המשתנה שמחזיק את כמות הפיקסלים הלבנים

current_pixel_count = white_pixels 

status_text = ""
text_color = (0, 255, 0) # ירוק כברירת מחדל

if current_pixel_count > FAIL_THRESHOLD:
    status_text = "FAIL"
    text_color = (0, 0, 255) # אדום (B, G, R)
    print(f"!!! DIAGNOSTIC RESULT: FAIL (Count {current_pixel_count} > {FAIL_THRESHOLD}) !!!")
else:
    status_text = "PASS"
    text_color = (0, 255, 0) # ירוק (B, G, R)
    print(f"DIAGNOSTIC RESULT: PASS (Count {current_pixel_count} <= {FAIL_THRESHOLD})")

# הוספת הכיתוב על התמונה המשולבת (בפינה השמאלית העליונה)
# הפרמטרים: התמונה, הטקסט, מיקום (x,y), פונט, גודל, צבע, עובי
cv2.putText(combined, f"Status: {status_text}", (30, 50), 
            cv2.FONT_HERSHEY_SIMPLEX, 1, text_color, 2)

# הוספת הכמות ליד הסטטוס (אופציונלי)
cv2.putText(combined, f"Count: {current_pixel_count}", (30, 90), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)

# ---------------------------------------------------------
    
# פונקציית העכבר המקורית שלך (לדגימת צבע)
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if x < display_width:
            scale_x = w_img / display_width
            scale_y = h_img / display_height
            orig_x = int(x * scale_x)
            orig_y = int(y * scale_y)
            
            # בדיקת גבולות כדי לא לקרוס
            if 0 <= orig_x < w_img and 0 <= orig_y < h_img:
                pixel = hsv[orig_y, orig_x]
                print(f"DEBUG: Pixel at ({orig_x},{orig_y}) -> H:{pixel[0]} S:{pixel[1]} V:{pixel[2]}")
        else:
            print("Clicked on mask area.")


# הצגה
window_name = "Result: Left=Original(Detected in Green), Right=Final Mask"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, pick_color)
cv2.imshow(window_name, combined)


print("Press any key to close...")
cv2.waitKey(0)
cv2.destroyAllWindows()
