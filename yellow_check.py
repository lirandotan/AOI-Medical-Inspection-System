# ### -------------- FINAL - PASS \ FAIL - WITHOUT CLASS B -------------------##############

# import cv2
# import numpy as np
# import os
# import hardware.buzzer as buzzer

# def check_yellow_defect(image_path):
    # print("🔍 [Vision] Step 1: ROI Crop & Advanced Color Analysis...")
    
    # img = cv2.imread(image_path)
    # if img is None:
        # print("   ❌ Error loading image")
        # return False

    # # הכנת נתיבים לשמירה (מבוסס על שם הקובץ המקורי)
    # dir_name = os.path.dirname(image_path)
    # base_name = os.path.basename(image_path)
    # name_no_ext = os.path.splitext(base_name)[0] # למשל corner_1
    
    # # נתיבים לקבצים החדשים
    # path_roi = os.path.join(dir_name, f"{name_no_ext}_ROI.PNG")
    # path_result = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

    # # ---------------------------------------------------------
    # # PART A: ROI CROP
    # # ---------------------------------------------------------
    # H, W = img.shape[:2]
    # roi_w = max(1, W // 5)
    # roi_h = max(1, H // 5)
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    
    # roi_img = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    
    # # --- שמירה 1: תמונת ה-ROI ---
    # cv2.imwrite(path_roi, roi_img)
    # print(f"    Saved ROI: {path_roi}")

    # # ---------------------------------------------------------
    # # PART B: בדיקה ולוגיקה
    # # ---------------------------------------------------------
    # h_low, h_high = 10, 37
    # s_low, s_high = 60, 199
    # v_low, v_high = 90, 199
    # MIN_AREA_THRESHOLD = 300
    # MAX_ASPECT_RATIO =  5.0 #3.8
    # FAIL_THRESHOLD_PIXELS = 1200

    # hsv = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)
    # bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

    # kernel = np.ones((5, 5), np.uint8)
    # opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
    # cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

    # final_mask = np.zeros_like(cleaned)
    # contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # for cnt in contours:
        # area = cv2.contourArea(cnt)
        # if area < MIN_AREA_THRESHOLD: continue
        
        # rect = cv2.minAreaRect(cnt)
        # (center), (w_rect, h_rect), angle = rect
        # if w_rect == 0 or h_rect == 0: continue
        # aspect_ratio = max(w_rect, h_rect) / min(w_rect, h_rect)

        # if aspect_ratio < MAX_ASPECT_RATIO:
            # cv2.drawContours(final_mask, [cnt], -1, 255, thickness=cv2.FILLED)

    # pixel_count = cv2.countNonZero(final_mask)
    
    # if pixel_count > FAIL_THRESHOLD_PIXELS:
        # status_text = "FAIL"
        # color_text = (0, 0, 255) # Red
        # result_bool = False
        # print(f"   ❌ FAIL: Yellow Defect Found (Count {pixel_count})")
    # else:
        # status_text = "PASS"
        # color_text = (0, 255, 0) # Green
        # result_bool = True
        # print("   ✅ PASS: No Yellow Defect")

    # # ---------------------------------------------------------
    # # PART C: באזר + שמירה + תצוגה
    # # ---------------------------------------------------------
    # print("   🔊 Buzzing...")
    # if result_bool: buzzer.beep_ok()
    # else: buzzer.beep_fail()

    # # יצירת התמונה המשולבת (Combined)
    # display_h = 400
    # ratio = display_h / roi_img.shape[0]
    # display_w = int(roi_img.shape[1] * ratio)

    # roi_small = cv2.resize(roi_img, (display_w, display_h))
    # mask_small = cv2.resize(final_mask, (display_w, display_h), interpolation=cv2.INTER_NEAREST)
    # mask_color = cv2.cvtColor(mask_small, cv2.COLOR_GRAY2BGR)

    # contours_draw, _ = cv2.findContours(mask_small, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(roi_small, contours_draw, -1, (0, 255, 0), 2)

    # combined = np.hstack((roi_small, mask_color))

    # cv2.putText(combined, f"Status: {status_text}", (10, 30), 
                # cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_text, 2)
    # cv2.putText(combined, f"Px: {pixel_count}", (10, 60), 
                # cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_text, 2)

    # # --- שמירה 2: תמונת התוצאה (Combined) ---
    # cv2.imwrite(path_result, combined)
    # print(f"    Saved Result: {path_result}")

    # # הצגה
    # # window_name = "Yellow Check Result"
    # # cv2.namedWindow(window_name)
    # # cv2.moveWindow(window_name, 50, 50)
    # # cv2.imshow(window_name, combined)
    
    # # print("   Press ANY KEY to continue...")
    # # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # return result_bool



# ######### GOOD - WITH CLASS A, CLASS B AND FAIL --------------------###############################################


# import cv2
# import numpy as np
# import os
# import hardware.buzzer as buzzer

# def check_yellow_defect(image_path):
    # print("🔍 [Vision] Step 1: ROI Crop & Advanced Color Analysis...")
    
    # img = cv2.imread(image_path)
    # if img is None:
        # print("    ❌ Error loading image")
        # return False

    # # הכנת נתיבים לשמירה
    # dir_name = os.path.dirname(image_path)
    # base_name = os.path.basename(image_path)
    # name_no_ext = os.path.splitext(base_name)[0]
    
    # path_roi = os.path.join(dir_name, f"{name_no_ext}_ROI.PNG")
    # path_result = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

    # # ---------------------------------------------------------
    # # PART A: ROI CROP
    # # ---------------------------------------------------------
    # H, W = img.shape[:2]
    # roi_w = max(1, W // 5)
    # roi_h = max(1, H // 5)
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    
    # roi_img = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    
    # # --- שמירה 1: תמונת ה-ROI ---
    # cv2.imwrite(path_roi, roi_img)
    # print(f"    Saved ROI: {path_roi}")

    # # ---------------------------------------------------------
    # # PART B: בדיקה ולוגיקה
    # # ---------------------------------------------------------
    # h_low, h_high = 10, 37
    # s_low, s_high = 60, 199
    # v_low, v_high = 90, 199
    
    # MIN_AREA_THRESHOLD = 300
    # MAX_ASPECT_RATIO =  5.0 
    
    # # --- עדכון: הגדרת שני ספים ---
    # LIMIT_CLASS_A = 1200  # עד כאן זה Class A (מושלם)
    # LIMIT_FAIL = 2500     # מעבר לזה זה פסילה, באמצע זה Class B

    # hsv = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)
    # bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

    # kernel = np.ones((5, 5), np.uint8)
    # opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
    # cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

    # final_mask = np.zeros_like(cleaned)
    # contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # for cnt in contours:
        # area = cv2.contourArea(cnt)
        # if area < MIN_AREA_THRESHOLD: continue
        
        # rect = cv2.minAreaRect(cnt)
        # (center), (w_rect, h_rect), angle = rect
        # if w_rect == 0 or h_rect == 0: continue
        # aspect_ratio = max(w_rect, h_rect) / min(w_rect, h_rect)

        # if aspect_ratio < MAX_ASPECT_RATIO:
            # cv2.drawContours(final_mask, [cnt], -1, 255, thickness=cv2.FILLED)

    # pixel_count = cv2.countNonZero(final_mask)
    
    # # --- עדכון: לוגיקה ל-3 מצבים ---
    # if pixel_count <= LIMIT_CLASS_A:
        # # מצב מושלם
        # status_text = "CLASS A"
        # color_text = (0, 255, 0) # Green
        # result_bool = True
        # print(f"    ✅ CLASS A: Perfect (Count {pixel_count})")
        
    # elif LIMIT_CLASS_A < pixel_count <= LIMIT_FAIL:
        # # מצב ביניים - יש שבר אבל עובר
        # status_text = "CLASS B"
        # color_text = (0, 165, 255) # Orange (BGR format)
        # result_bool = True
        # print(f"    ⚠️ CLASS B: Minor Defect (Count {pixel_count})")
        
    # else:
        # # מצב נכשל
        # status_text = "FAIL"
        # color_text = (0, 0, 255) # Red
        # result_bool = False
        # print(f"    ❌ FAIL: Large Defect (Count {pixel_count})")

    # # ---------------------------------------------------------
    # # PART C: באזר + שמירה + תצוגה
    # # ---------------------------------------------------------
    # print("    🔊 Buzzing...")
    # # כאן אנחנו מחליטים שגם Class B נותן צפצוף "תקין"
    # if result_bool: 
        # buzzer.beep_ok()
    # else: 
        # buzzer.beep_fail()

    # # יצירת התמונה המשולבת (Combined)
    # display_h = 400
    # ratio = display_h / roi_img.shape[0]
    # display_w = int(roi_img.shape[1] * ratio)

    # roi_small = cv2.resize(roi_img, (display_w, display_h))
    # mask_small = cv2.resize(final_mask, (display_w, display_h), interpolation=cv2.INTER_NEAREST)
    # mask_color = cv2.cvtColor(mask_small, cv2.COLOR_GRAY2BGR)

    # contours_draw, _ = cv2.findContours(mask_small, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # # נצייר את הקונטורים בצבע הטקסט (ירוק/כתום/אדום) כדי שיהיה ברור ויזואלית
    # cv2.drawContours(roi_small, contours_draw, -1, color_text, 2)

    # combined = np.hstack((roi_small, mask_color))

    # cv2.putText(combined, f"Status: {status_text}", (10, 30), 
                # cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_text, 2)
    # cv2.putText(combined, f"Px: {pixel_count}", (10, 60), 
                # cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_text, 2)
    
    # # # הוספת הסברים על הספים בתמונה
    # # info_str = f"A<={LIMIT_CLASS_A} | Fail>{LIMIT_FAIL}"
    # # cv2.putText(combined, info_str, (10, 380), 
                # # cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    # # --- שמירה 2: תמונת התוצאה (Combined) ---
    # cv2.imwrite(path_result, combined)
    # print(f" Saved Result: {path_result}")

    # cv2.destroyAllWindows()

    # return status_text  # יחזיר "CLASS A", "CLASS B", או "FAIL"


###-----------------FINAL CODE: YELLOW - WITH COMMENTS ----------------------------####################

######### WITH CLASS A, CLASS B AND FAIL --------------------###############################################

import cv2
import numpy as np
import os
import hardware.buzzer as buzzer

def check_yellow_defect(image_path):
    print("🔍 [Vision] Step 1: ROI Crop & Advanced Color Analysis...")
    
    img = cv2.imread(image_path)
    if img is None:
        print("    ❌ Error loading image")
        return False

    # Prepare paths for saving
    dir_name = os.path.dirname(image_path)
    base_name = os.path.basename(image_path)
    name_no_ext = os.path.splitext(base_name)[0]
    
    path_roi = os.path.join(dir_name, f"{name_no_ext}_ROI.PNG")
    path_result = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

    # ---------------------------------------------------------
    # PART A: ROI CROP
    # ---------------------------------------------------------
    H, W = img.shape[:2]
    roi_w = max(1, W // 5)
    roi_h = max(1, H // 5)
    x_start = (W - roi_w) // 2
    y_start = (H - roi_h) // 2
    
    roi_img = img[y_start:y_start+roi_h, x_start:x_start+roi_w].copy()
    
    # --- Save 1: ROI Image ---
    cv2.imwrite(path_roi, roi_img)
    print(f"    Saved ROI: {path_roi}")

    # ---------------------------------------------------------
    # PART B: Testing and Logic
    # ---------------------------------------------------------
    h_low, h_high = 10, 37
    s_low, s_high = 60, 199
    v_low, v_high = 90, 199
    
    MIN_AREA_THRESHOLD = 300
    MAX_ASPECT_RATIO =  3.8 #5.0 
    
    # --- Update: Definition of two thresholds ---
    LIMIT_CLASS_B = 1200  # Up to here is Class A (Perfect)
    LIMIT_FAIL = 2500     # Beyond this is a Failure; in between is Class B

    hsv = cv2.cvtColor(roi_img, cv2.COLOR_BGR2HSV)
    bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

    # Morphological operations to clean noise
    kernel = np.ones((5, 5), np.uint8)
    opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)
    cleaned = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)

    final_mask = np.zeros_like(cleaned)
    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < MIN_AREA_THRESHOLD: continue
        
        rect = cv2.minAreaRect(cnt)
        (center), (w_rect, h_rect), angle = rect
        if w_rect == 0 or h_rect == 0: continue
        aspect_ratio = max(w_rect, h_rect) / min(w_rect, h_rect)

        # Filter by aspect ratio to ignore elongated noise
        if aspect_ratio < MAX_ASPECT_RATIO:
            cv2.drawContours(final_mask, [cnt], -1, 255, thickness=cv2.FILLED)

    pixel_count = cv2.countNonZero(final_mask)
    
    # --- Update: Logic for 3 states ---
    if pixel_count <= LIMIT_CLASS_B:
        # Perfect state
        status_text = "CLASS A"
        color_text = (0, 255, 0) # Green
        result_bool = True
        print(f"    ✅ CLASS A: Perfect (Count {pixel_count})")
        
    elif LIMIT_CLASS_B < pixel_count <= LIMIT_FAIL:
        # Intermediate state - there is a fracture but it passes
        status_text = "CLASS B"
        color_text = (0, 165, 255) # Orange (BGR format)
        result_bool = True
        print(f"    ⚠️ CLASS B: Minor Defect (Count {pixel_count})")
        
    else:
        # Fail state
        status_text = "FAIL"
        color_text = (0, 0, 255) # Red
        result_bool = False
        print(f"    ❌ FAIL: Large Defect (Count {pixel_count})")

    # ---------------------------------------------------------
    # PART C: Buzzer + Save + Display
    # ---------------------------------------------------------
    print("    🔊 Buzzing...")
    # Here we decide that Class B also gives an "OK" beep
    if status_text == "FAIL":
        buzzer.beep_fail()   # שני צפצופים
    elif status_text == "CLASS B":
        buzzer.beep_warning() # צפצוף אחד
    else:
        pass # CLASS A - שקט מוחלט


    # Create the combined display image
    display_h = 400
    ratio = display_h / roi_img.shape[0]
    display_w = int(roi_img.shape[1] * ratio)

    roi_small = cv2.resize(roi_img, (display_w, display_h))
    mask_small = cv2.resize(final_mask, (display_w, display_h), interpolation=cv2.INTER_NEAREST)
    mask_color = cv2.cvtColor(mask_small, cv2.COLOR_GRAY2BGR)

    contours_draw, _ = cv2.findContours(mask_small, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours in the status color (Green/Orange/Red) for visual clarity
    cv2.drawContours(roi_small, contours_draw, -1, color_text, 2)

    combined = np.hstack((roi_small, mask_color))

    cv2.putText(combined, f"Status: {status_text}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color_text, 2)
    cv2.putText(combined, f"Px: {pixel_count}", (10, 60), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color_text, 2)
    
    # --- Save 2: Result Image (Combined) ---
    cv2.imwrite(path_result, combined)
    print(f" Saved Result: {path_result}")

    cv2.destroyAllWindows()

    return status_text  # Will return "CLASS A", "CLASS B", or "FAIL"
