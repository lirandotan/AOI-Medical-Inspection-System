###### --------------- ONLY YELLOW CHECK (WITHOUT MORPOLOGY) !! ------------------###########

##### ---------------- ANALYZE LIVE OR Existing FILE -----------------###########

# import os
# import time

# # ייבוא המודולים
# import hardware.camera as cam
# import hardware.motor as motor
# import hardware.buzzer as buzzer
# import vision.yellow_check as yellow_algo
# # import vision.morphology as morph_algo  <-- הוסר כי לא בשימוש יותר

# # ---------------------------------------------------------
# # הגדרות
# # ---------------------------------------------------------
# NUM_CORNERS = 4          # מספר הפינות לבדיקה (במצב לייב)
# STEPS_PER_90_DEG = 1600   # כיול מנוע
# RESULTS_BASE_FOLDER = "Test_Results" 

# def analyze_image(filename, corner_id="N/A"):
    # """
    # פונקציה שמבצעת את בדיקת הצבע בלבד.
    # מחזירה True אם התמונה תקינה (אין צהוב חשוד), ו-False אם נמצא פגם.
    # """
    # print(f" -> Analyzing image: {os.path.basename(filename)}...")

    # # --- בדיקת צבע (הלב של האנליזה) ---
    # is_color_ok = yellow_algo.check_yellow_defect(filename)
    
    # if not is_color_ok:
        # print(f"⛔ FAIL: Yellow Defect Detected (Corner/File: {corner_id}).")
        # return False

    # # אם הגענו לכאן - עברנו את בדיקת הצבע והכל תקין
    # print(f"✅ PASS: Color OK (Corner/File: {corner_id}).")
    # return True

# def run_live_inspection():
    # """
    # מריץ את תהליך הבדיקה המלא: קלט מספר סידורי, יצירת תיקייה, סיבוב מנוע וצילום.
    # """
    # # 1. קליטת מספר סידורי (SN)
    # serial_number = input("Enter Component Serial Number (SN): ").strip()
    # if not serial_number: serial_number = "Unknown_Device"

    # # 2. יצירת תיקייה ייעודית לרכיב
    # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
    
    # if not os.path.exists(component_folder):
        # os.makedirs(component_folder)
        # print(f" Created folder: {component_folder}")
    # else:
        # print(f" Saving to existing folder: {component_folder}")

    # for i in range(NUM_CORNERS):
        # corner_id = i + 1
        # print(f"\n Processing Corner {corner_id}/{NUM_CORNERS}")
        
        # # הגדרת נתיב השמירה
        # filename = os.path.join(component_folder, f"corner_{corner_id}.PNG")
        
        # # --- שלב צילום ---
        # success = cam.take_picture(filename)
        # if not success:
            # print("⛔ CRITICAL ERROR: Camera failed.")
            # buzzer.beep_fail()
            # return # יציאה מהפונקציה

        # # --- ביצוע אנליזה (בדיקת צהוב בלבד) ---
        # is_pass = analyze_image(filename, corner_id)

        # if not is_pass:
            # buzzer.beep_fail()
            # print(f"⛔ STOPPING process due to defect.")
            # return # עוצר את הלולאה ואת הבדיקה

        # # --- סיבוב מנוע (רק אם יש עוד פינות ועדיין לא נכשלנו) ---
        # if i < NUM_CORNERS - 1:
            # print(" Rotating to next corner...")
            # motor.move_steps(STEPS_PER_90_DEG, direction="CW")
            # time.sleep(1)

    # # אם סיימנו את הלולאה בלי return, הכל תקין
    # print(f"\n✅✅✅ Component {serial_number}: PASSED. ✅✅✅")

# def run_file_analysis():
    # """
    # מבקש נתיב לתמונה ומריץ עליה את בדיקת הצהוב בלבד (בלי מנוע/מצלמה).
    # """
    # image_path = input("Enter full path to image (drag & drop file here): ").strip()
    
    # # הסרת מרכאות אם המשתמש גרר את הקובץ (Windows מוסיף לפעמים מרכאות)
    # image_path = image_path.replace('"', '').replace("'", "")

    # if not os.path.exists(image_path):
        # print("❌ Error: File does not exist.")
        # return

    # print("\n--- Starting File Analysis ---")
    # is_pass = analyze_image(image_path, corner_id="File_Mode")

    # if is_pass:
        # print("\n✅ Image Analysis: PASSED.")
    # else:
        # print("\n⛔ Image Analysis: FAILED.")
        # #buzzer.beep_fail() # אופציונלי - אם אתה רוצה צפצוף גם במצב קובץ

# def main():
    # os.system('clear' if os.name == 'posix' else 'cls')
    # print("=== PDA Inspection System (Yellow Check Only) ===")
    
    # buzzer.init()
    
    # try:
        # print("Select Mode:")
        # print("1. Live Inspection (Camera + Motor)")
        # print("2. Analyze Existing Image (File)")
        
        # choice = input("Choice (1/2): ").strip()

        # if choice == '1':
            # run_live_inspection()
        # elif choice == '2':
            # run_file_analysis()
        # else:
            # print("Invalid choice. Exiting.")

    # except KeyboardInterrupt:
        # print("\n User interrupted process.")
    
    # finally:
        # buzzer.close()
        # print("System shutdown safely.")

# if __name__ == "__main__":
    # main()





# ##### ---------------- ANALYZE LIVE OR Existing FILE -----------------###########

# import os
# import time

# # ייבוא המודולים
# import hardware.camera as cam
# import hardware.motor as motor
# import hardware.buzzer as buzzer
# import vision.yellow_check as yellow_algo
# import vision.morphology as morph_algo

# # ---------------------------------------------------------
# # הגדרות
# # ---------------------------------------------------------
# NUM_CORNERS = 1          # מספר הפינות לבדיקה (במצב לייב)
# STEPS_PER_90_DEG = 400   # כיול מנוע
# RESULTS_BASE_FOLDER = "Test_Results" 

# def analyze_image(filename, corner_id="N/A"):
    # """
    # פונקציה שמבצעת את כל שרשרת האלגוריתמים על תמונה נתונה.
    # מחזירה True אם התמונה תקינה, ו-False אם נמצא פגם.
    # """
    # print(f" -> Analyzing image: {os.path.basename(filename)}...")

    # # --- שלב 1: בדיקת צבע (הקובץ המתוקן עם הסינון) ---
    # is_color_ok = yellow_algo.check_yellow_defect(filename)
    
    # if not is_color_ok:
        # print(f"⛔ FAIL: Yellow Defect Detected (Corner/File: {corner_id}).")
        # return False

    # # --- שלב 2: יצירת מסכה ---
    # mask_path = morph_algo.create_binary_mask(filename)
    # if mask_path is None:
        # print(f"⛔ FAIL: Failed to create mask (Corner/File: {corner_id}).")
        # return False

    # # --- שלב 3: בדיקת שלד ---
    # is_skel_ok = morph_algo.check_skeleton_continuity(mask_path)
    # if not is_skel_ok:
        # print(f"⛔ FAIL: Skeleton Check Failed (Corner/File: {corner_id}).")
        # return False

    # # אם הגענו לכאן - הכל תקין
    # return True

# def run_live_inspection():
    # """
    # מריץ את תהליך הבדיקה המלא: קלט מספר סידורי, יצירת תיקייה, סיבוב מנוע וצילום.
    # """
    # # 1. קליטת מספר סידורי (SN)
    # serial_number = input("Enter Component Serial Number (SN): ").strip()
    # if not serial_number: serial_number = "Unknown_Device"

    # # 2. יצירת תיקייה ייעודית לרכיב
    # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
    
    # if not os.path.exists(component_folder):
        # os.makedirs(component_folder)
        # print(f" Created folder: {component_folder}")
    # else:
        # print(f" Saving to existing folder: {component_folder}")

    # for i in range(NUM_CORNERS):
        # corner_id = i + 1
        # print(f"\n Processing Corner {corner_id}/{NUM_CORNERS}")
        
        # # הגדרת נתיב השמירה
        # filename = os.path.join(component_folder, f"corner_{corner_id}.PNG")
        
        # # --- שלב צילום ---
        # success = cam.take_picture(filename)
        # if not success:
            # print("⛔ CRITICAL ERROR: Camera failed.")
            # buzzer.beep_fail()
            # return # יציאה מהפונקציה

        # # --- ביצוע אנליזה (קריאה לפונקציה המשותפת) ---
        # is_pass = analyze_image(filename, corner_id)

        # if not is_pass:
            # buzzer.beep_fail()
            # print(f"⛔ STOPPING process due to defect.")
            # return # עוצר את הלולאה ואת הבדיקה

        # # --- סיבוב מנוע (רק אם יש עוד פינות ועדיין לא נכשלנו) ---
        # if i < NUM_CORNERS - 1:
            # print(" Rotating to next corner...")
            # motor.move_steps(STEPS_PER_90_DEG, direction="CW")
            # time.sleep(1)

    # # אם סיימנו את הלולאה בלי return, הכל תקין
    # print(f"\n✅✅✅ Component {serial_number}: PASSED. ✅✅✅")

# def run_file_analysis():
    # """
    # מבקש נתיב לתמונה ומריץ עליה את האלגוריתמים בלבד (בלי מנוע/מצלמה).
    # """
    # image_path = input("Enter full path to image (drag & drop file here): ").strip()
    
    # # הסרת מרכאות אם המשתמש גרר את הקובץ (Windows מוסיף לפעמים מרכאות)
    # image_path = image_path.replace('"', '').replace("'", "")

    # if not os.path.exists(image_path):
        # print("❌ Error: File does not exist.")
        # return

    # print("\n--- Starting File Analysis ---")
    # is_pass = analyze_image(image_path, corner_id="File_Mode")

    # if is_pass:
        # print("\n✅ Image Analysis: PASSED.")
    # else:
        # print("\n⛔ Image Analysis: FAILED.")
        # #buzzer.beep_fail() # אופציונלי - אם אתה רוצה צפצוף גם במצב קובץ

# def main():
    # os.system('clear' if os.name == 'posix' else 'cls')
    # print("=== PDA Inspection System ===")
    
    # buzzer.init()
    
    # try:
        # print("Select Mode:")
        # print("1. Live Inspection (Camera + Motor)")
        # print("2. Analyze Existing Image (File)")
        
        # choice = input("Choice (1/2): ").strip()

        # if choice == '1':
            # run_live_inspection()
        # elif choice == '2':
            # run_file_analysis()
        # else:
            # print("Invalid choice. Exiting.")

    # except KeyboardInterrupt:
        # print("\n User interrupted process.")
    
    # finally:
        # buzzer.close()
        # print("System shutdown safely.")

# if __name__ == "__main__":
    # main()





##########-----------------ONLY FOR LIVE TAKE PIC - NOT FOR Existing FILE----------------------------##############



# import os
# import time

# # ייבוא המודולים
# import hardware.camera as cam
# import hardware.motor as motor
# import hardware.buzzer as buzzer
# import vision.yellow_check as yellow_algo
# import vision.morphology as morph_algo

# def main():
    # os.system('clear' if os.name == 'posix' else 'cls')
    # print("=== PDA Inspection System ===")
    
    # # ---------------------------------------------------------
    # # הגדרות
    # # ---------------------------------------------------------
    # NUM_CORNERS = 1          # מספר הפינות לבדיקה
    # STEPS_PER_90_DEG = 400   # כיול מנוע
    # RESULTS_BASE_FOLDER = "Test_Results" 
    # # ---------------------------------------------------------

    # # 1. קליטת מספר סידורי (SN)
    # serial_number = input("Enter Component Serial Number (SN): ").strip()
    # if not serial_number: serial_number = "Unknown_Device"

    # # 2. יצירת תיקייה ייעודית לרכיב הזה
    # # כל התמונות והמסכות יישמרו כאן!
    # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
    
    # if not os.path.exists(component_folder):
        # os.makedirs(component_folder)
        # print(f" Created folder: {component_folder}")
    # else:
        # print(f" Saving to existing folder: {component_folder}")

    # buzzer.init()
    
    # try:
        # for i in range(NUM_CORNERS):
            # corner_id = i + 1
            # print(f"\n Processing Corner {corner_id}/{NUM_CORNERS}")
            
            # # הגדרת נתיב השמירה בתוך התיקייה הספציפית
            # filename = os.path.join(component_folder, f"corner_{corner_id}.PNG")
            
            # # --- שלב 1: צילום ושמירה ---
            # # הפונקציה מצלמת ושומרת את הקובץ בנתיב המלא שנתנו לה (בתוך התיקייה)
            # success = cam.take_picture(filename)
            # if not success:
                # print("⛔ CRITICAL ERROR: Camera failed.")
                # buzzer.beep_fail()
                # break

            # # --- שלב 2: בדיקת צבע (הקובץ המתוקן עם הסינון) ---
            # # הבאזר יצפצף מתוך הפונקציה הזו
            # is_color_ok = yellow_algo.check_yellow_defect(filename)
            
            # if not is_color_ok:
                # print(f"⛔ STOPPING at Corner {corner_id}: Yellow Defect Detected.")
                # break

            # # --- שלב 3: יצירת מסכה ---
            # mask_path = morph_algo.create_binary_mask(filename)
            # if mask_path is None:
                # print(f"⛔ STOPPING: Failed to create mask.")
                # buzzer.beep_fail()
                # break

            # # --- שלב 4: בדיקת שלד ---
            # is_skel_ok = morph_algo.check_skeleton_continuity(mask_path)
            # if not is_skel_ok:
                # print(f"⛔ STOPPING at Corner {corner_id}: Skeleton Check Failed.")
                # break

            # # --- סיבוב מנוע ---
            # if i < NUM_CORNERS - 1:
                # print(" Rotating to next corner...")
                # motor.move_steps(STEPS_PER_90_DEG, direction="CW")
                # time.sleep(1)

        # else:
            # print(f"\n✅✅✅ Component {serial_number}: PASSED. ✅✅✅")

    # except KeyboardInterrupt:
        # print("\n User interrupted process.")
    
    # finally:
        # buzzer.close()
        # print("System shutdown safely.")

# if __name__ == "__main__":
    # main()



########--------------	FINAL CODE !!  ---  FIFFERENT NUM OF STES PER CORNER ---------------------########

import os
import time
import hardware.camera as cam
import hardware.motor as motor
import hardware.buzzer as buzzer
import vision.yellow_check as yellow_algo

# ---------------------------------------------------------
# הגדרות
# ---------------------------------------------------------
NUM_CORNERS = 4 #4          
RESULTS_BASE_FOLDER = "Test_Results" 

def analyze_image(filename, corner_id="N/A"):
    print(f" -> Analyzing: {os.path.basename(filename)}...")
    # האלגוריתם מחזיר עכשיו מחרוזת, והוא כבר מצפצף בעצמו
    status_result = yellow_algo.check_yellow_defect(filename)
    
    if status_result == "FAIL":
        print(f"⛔ FAIL: Defect Detected at Corner {corner_id}.")
        return False

    # גם CLASS A וגם CLASS B נחשבים כ-True עבור ה-Main (ממשיכים לעבוד)
    print(f"✅ PASS ({status_result}): Corner {corner_id} OK.")
    return True
# def analyze_image(filename, corner_id="N/A"):
    # print(f" -> Analyzing: {os.path.basename(filename)}...")
    # is_color_ok = yellow_algo.check_yellow_defect(filename)
    
    # if not is_color_ok:
        # print(f"⛔ FAIL: Defect Detected at Corner {corner_id}.")
        # return False

    # print(f"✅ PASS: Corner {corner_id} OK.")
    # return True

def run_live_inspection():
    # 1. איפוס המנוע לוגית (אנחנו מניחים שהתחלנו מנקודת האפס הפיזית)
    motor.reset_sequence()

    serial_number = input("Enter SN: ").strip() or "Unknown"
    component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
    
    if not os.path.exists(component_folder):
        os.makedirs(component_folder)

    defect_found = False # דגל לבדיקה אם היה כישלון

    # --- לולאת הבדיקה ---
    for i in range(NUM_CORNERS):
        corner_id = i + 1
        print(f"\n Processing Corner {corner_id}/{NUM_CORNERS}")
        
        filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
        
        # א. צילום
        if not cam.take_picture(filename):
            print("⛔ Camera Error.")
            buzzer.beep_fail()
            defect_found = True
            break # יוצאים מהלולאה

        # ב. אנליזה
        if not analyze_image(filename, corner_id):
            #buzzer.beep_fail()
            defect_found = True
            break # יוצאים מהלולאה (הכישלון גורם לעצירה)

        # ג. סיבוב לפינה הבאה (רק אם זו לא הפינה האחרונה לבדיקה)
        # שים לב: אנחנו מסובבים כדי להכין את הפינה הבאה לצילום
        if i < NUM_CORNERS - 1:
            motor.rotate_to_next_corner()
            time.sleep(1)

    # --- סיום התהליך ---
    
    if defect_found:
        print(f"\n⛔ Result: Component {serial_number} FAILED.")
    else:
        print(f"\n✅ Result: Component {serial_number} PASSED ALL CHECKS.")

    # --- חזרה לנקודת ההתחלה (הדרישה החדשה) ---
    # הפקודה הזו תשלים את הסיבובים שנשארו עד שנגיע חזרה ל-0
    motor.finish_cycle()

# --- שאר הקוד (run_file_analysis, main) ללא שינוי ---
def run_file_analysis():
    image_path = input("Path to image: ").strip().replace('"', '').replace("'", "")
    if os.path.exists(image_path):
        if analyze_image(image_path, "File_Mode"):
            print("✅ PASSED.")
        else:
            print("⛔ FAILED.")
    else:
        print("❌ File not found.")

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    buzzer.init()
    try:
        choice = input("1. Live Inspection\n2. File Analysis\nChoice: ").strip()
        if choice == '1': run_live_inspection()
        elif choice == '2': run_file_analysis()
    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        buzzer.close()

if __name__ == "__main__":
    main()
