# import customtkinter as ctk
# from PIL import Image
# import os

# # --- הגדרות עיצוב כלליות ---
# ctk.set_appearance_mode("Dark")  # מצב כהה (Dark Mode)
# ctk.set_default_color_theme("blue")  # צבע אלמנטים (כחול פיליפס)

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות החלון הראשי
        # self.title("Philips - PDA Chipping Inspection")
        # self.geometry("800x600") # גודל החלון בהתחלה
        # # self.attributes('-fullscreen', True) # אם תרצי מסך מלא בעתיד, תבטלי את ההערה הזו

        # # הגדרת גריד (רשת) - מחלקים את המסך לשורות ועמודות
        # # זה עוזר לנו למקם דברים במרכז או בצדדים
        # self.grid_columnconfigure(0, weight=1) # עמודה אחת גמישה
        # self.grid_rowconfigure(1, weight=1)    # שורה אמצעית גמישה

        # # ============================================================
        # # חלק א': הכותרת (Header) והלוגו
        # # ============================================================
        
        # # טעינת התמונה (נשמור אותה כמשתנה במחלקה)
        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # # אנחנו טוענים את התמונה ומגדירים לה גודל לתצוגה (למשל רוחב 200)
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(250, 80)) # גודל הלוגו בפיקסלים
        # except Exception as e:
            # print(f"Error loading logo: {e}")
            # self.logo_image = None

        # # יצירת מסגרת (Frame) לכותרת העליונה
        # self.header_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, sticky="ew", padx=20, pady=20)

        # # הצגת הלוגו (בתוך לייבל)
        # if self.logo_image:
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="left") # הצמדה לשמאל

        # # כותרת טקסט ליד הלוגו
        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(size=24, weight="bold"))
        # self.label_title.pack(side="left", padx=20)

        # # ============================================================
        # # חלק ב': המסך הראשי (Dashboard)
        # # ============================================================
        
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=10)

        # # אזור להכנסת מספר סידורי (SN)
        # self.entry_sn = ctk.CTkEntry(self.main_frame, placeholder_text="Enter Serial Number (SN)", width=300, height=40)
        # self.entry_sn.pack(pady=20)

        # # כפתור התחלה ענק
        # self.btn_start = ctk.CTkButton(self.main_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=20, weight="bold"),
                                       # width=250, height=60,
                                       # fg_color="green", hover_color="darkgreen", # צבע ירוק
                                       # command=self.start_process_clicked) # פונקציה שתקרה כשלוחצים
        # self.btn_start.pack(pady=10)

        # # אזור סטטוס (איפה שנכתוב Pass/Fail ואיזה פינה אנחנו)
        # self.status_label = ctk.CTkLabel(self.main_frame, text="Ready to Scan", font=ctk.CTkFont(size=18))
        # self.status_label.pack(pady=20)

        # # בר התקדמות (Progress Bar) - כרגע ריק
        # self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=400)
        # self.progress_bar.set(0) # מאופס
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # פונקציות (כאן תהיה הלוגיקה בהמשך)
    # # ============================================================
    # def start_process_clicked(self):
        # print("Button Clicked! (Logic to be added later)")
        # self.status_label.configure(text="System Started...")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()



############-------------------------------------------------------------############

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys

# # --- הגדרות עיצוב כלליות ---
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון - מסך מלא
        # self.title("Philips - PDA Chipping Inspection")
        
        # # הגדרת מסך מלא
        # self.attributes('-fullscreen', True)
        
        # # אפשרות יציאה בחירום (מקש ESC)
        # self.bind("<Escape>", lambda event: self.destroy())

        # # הגדרת גריד ראשית - מאפשרת למרכז דברים
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=0) # שורה לכותרת
        # self.grid_rowconfigure(1, weight=1) # שורה לתוכן הראשי (גמישה)
        # self.grid_rowconfigure(2, weight=0) # שורה תחתונה

        # # ============================================================
        # # חלק א': כפתור יציאה (למעלה בימין)
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="X", width=40, height=40,
                                      # fg_color="red", command=self.close_app)
        # self.btn_exit.place(relx=0.98, rely=0.02, anchor="ne") # ממוקם בפינה הימנית

        # # ============================================================
        # # חלק ב': הכותרת והלוגו (עכשיו אנכיים)
        # # ============================================================
        
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(50, 20)) # קצת רווח מלמעלה

        # # 1. לוגו
        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # # הגדלתי קצת את הלוגו שיראה טוב במסך מלא
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(400, 130)) 
            
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=10) # side="top" שם אותו למעלה
            
        # except Exception as e:
            # print(f"Error loading logo: {e}")

        # # 2. כותרת (מתחת ללוגו)
        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=32, weight="bold"))
        # self.label_title.pack(side="top", pady=10)

        # # ============================================================
        # # חלק ג': המסך הראשי (Dashboard)
        # # ============================================================
        
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0) # ממורכז אוטומטית בגלל הגריד

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.main_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center",
                                     # font=ctk.CTkFont(size=20),
                                     # width=400, height=50)
        # self.entry_sn.pack(pady=30)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.main_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=70,
                                       # fg_color="#0066cc", hover_color="#004c99", # כחול פיליפס
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.main_frame, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=20)

        # # בר התקדמות
        # self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=600, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=20)

    # # ============================================================
    # # פונקציות
    # # ============================================================
    # def start_process_clicked(self):
        # self.status_label.configure(text="Initializing Camera & Motor...", text_color="yellow")
        # self.progress_bar.start()

    # def close_app(self):
        # self.destroy() # סוגר את החלון
        # sys.exit()

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


######-------------------------------------------------------------------------------------################

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading

# # --- ייבוא החומרה והאלגוריתם (מהקודים שלך) ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")
    # print("Make sure gui_app.py is in the same folder as 'hardware' and 'vision' folders!")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        
        # # תיקון לבאג המסך המלא: מפעיל את המסך המלא בדיליי קצר
        # self.after(100, lambda: self.attributes('-fullscreen', True))
        
        # # יציאה בחירום
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1) 

        # # ============================================================
        # # כפתורי שליטה (יציאה ומזעור) - פינה ימנית עליונה
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=20, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.02, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=20, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.92, rely=0.02, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(40, 10))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(350, 110))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=28, weight="bold"))
        # self.label_title.pack(side="top", pady=5)

        # # ============================================================
        # # חלק ב': המסך הראשי
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0)

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.main_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack(pady=20)

        # # אזור לתצוגת התמונה (ריק בהתחלה)
        # self.image_display = ctk.CTkLabel(self.main_frame, text="Waiting for scan...", 
                                          # width=400, height=300, fg_color="gray20", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.main_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_thread) # קורא ל-Thread
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.main_frame, text="System Ready", 
                                         # font=ctk.CTkFont(size=22))
        # self.status_label.pack(pady=10)

        # # בר התקדמות
        # self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=600, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה ו-Threading
    # # ============================================================
    
    # def minimize_app(self):
        # """מזעור החלון"""
        # self.iconify()

    # def close_app(self):
        # """סגירה מסודרת"""
        # try:
            # motor.finish_cycle() # מוודא שהמנוע חוזר ל-0 לפני יציאה
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def start_process_thread(self):
        # """פונקציה שמתחילה את התהליך ברקע"""
        # sn = self.entry_sn.get().strip()
        # if not sn:
            # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
            # return

        # # נועלים את הכפתור כדי שלא ילחצו פעמיים
        # self.btn_start.configure(state="disabled", text="RUNNING...")
        # self.entry_sn.configure(state="disabled")
        
        # # מתחילים תהליכון (Thread)
        # threading.Thread(target=self.run_logic, args=(sn,), daemon=True).start()

    # def run_logic(self, serial_number):
        # """
        # כאן רצה הלוגיקה האמיתית של המכונה (בנפרד מה-GUI)
        # """
        # try:
            # # 1. הכנות
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # # 2. הלולאה (4 פינות)
            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                
                # # א. עדכון סטטוס
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # # ב. צילום
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # # ג. עיבוד תמונה
                # # הערה: האלגוריתם שלך שומר את התמונה המעובדת עם סיומת _YELLOW_RESULT.PNG
                # # אנחנו נטען אותה משם כדי להציג במסך
                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # # נסיון להציג את התמונה המעובדת על המסך
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break # עוצרים אם יש תקלה
                # else:
                    # buzzer.beep_ok()

                # # ד. סיבוב (אם לא סיימנו)
                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # # אנימציה קטנה בפס התקדמות בזמן הסיבוב
                    # motor.rotate_to_next_corner()
            
            # # 3. סיום
            # self.update_progress(1.0)
            # motor.finish_cycle() # חזרה ל-0

            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # # שחרור הכפתורים בסוף
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))

    # # --- פונקציות עזר לעדכון ה-GUI מתוך ה-Thread ---
    
    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # # טעינת התמונה והקטנה שלה שתתאים לחלון
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(400, 300))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


########-------------------------------------------------------------------------##########

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# # הגדרה שהופכת את ה-GUI למותאם למסכים ברזולוציה גבוהה
# ctk.set_widget_scaling(1.0) 
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        
        # # --- תיקון למסך מלא ---
        # # אנחנו מגדירים מסך מלא מיד, וגם מוודאים זאת שוב אחרי חצי שנייה
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        
        # # יציאה בחירום
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1) 

        # # ============================================================
        # # שלושת כפתורי השליטה (יציאה, שינוי גודל, מזעור)
        # # ============================================================
        
        # # 1. כפתור יציאה (X)
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # # 2. כפתור שינוי גודל / מסך מלא (ם)
        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # # 3. כפתור מזעור (—)
        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(40, 10))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(350, 110))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=32, weight="bold"))
        # self.label_title.pack(side="top", pady=5)

        # # ============================================================
        # # חלק ב': המסך הראשי
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0)

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.main_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack(pady=15)

        # # --- אזור לתצוגת התמונה ---
        # # הגדלנו את המסגרת
        # self.image_display = ctk.CTkLabel(self.main_frame, text="Waiting for scan...", 
                                          # width=800, height=500, # גודל התחלתי גדול יותר
                                          # fg_color="gray20", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.main_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_thread) 
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.main_frame, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # # בר התקדמות
        # self.progress_bar = ctk.CTkProgressBar(self.main_frame, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # פונקציות GUI
    # # ============================================================
    
    # def minimize_app(self):
        # """מזעור החלון"""
        # self.iconify()

    # def toggle_fullscreen(self):
        # """מעבר בין מסך מלא לחלון רגיל"""
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # """סגירה מסודרת"""
        # try:
            # motor.finish_cycle() 
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # # ============================================================
    # # לוגיקה ו-Threading
    # # ============================================================

    # def start_process_thread(self):
        # sn = self.entry_sn.get().strip()
        # if not sn:
            # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
            # return

        # self.btn_start.configure(state="disabled", text="RUNNING...")
        # self.entry_sn.configure(state="disabled")
        
        # threading.Thread(target=self.run_logic, args=(sn,), daemon=True).start()

    # def run_logic(self, serial_number):
        # try:
            # # 1. הכנות
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # # 2. הלולאה (4 פינות)
            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # # א. צילום
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # # ב. עיבוד תמונה
                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # # הצגת התמונה - קריאה לפונקציה המעודכנת
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # # ג. סיבוב
                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # # 3. סיום וחזרה
            # self.update_progress(1.0)

            # # --- הוספת ההודעה שביקשת ---
            # self.update_status("Returning to Start Position...", "orange")
            
            # # רק לאחר עדכון ההודעה, מבצעים את החזרה
            # time.sleep(0.5) # השהייה קטנה כדי שיראו את ההודעה
            # motor.finish_cycle() 

            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))

    # # --- פונקציות עזר ---
    
    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # """טעינת תמונה והצגתה בגודל גדול"""
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # # שינוי הגודל כאן - הגדלתי ל-800x500
                # # שימי לב: זה ישמור על פרופורציות אם התמונה המקורית שונה,
                # # אבל ימתח אותה למסגרת הזו.
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(800, 500))
                
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


##############----------------------------------------------------------------------------##############

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # # חלוקה ראשית של הגריד
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(20, 10))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(300, 90))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=28, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי (מחולק לשמאל וימין)
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=20)
        
        # # חלוקה לעמודות בתוך האזור הראשי:
        # # עמודה 0: רשימת הפינות (צרה יותר)
        # # עמודה 1: התמונה והכפתורים (רחבה)
        # self.main_frame.grid_columnconfigure(0, weight=1) # צד שמאל
        # self.main_frame.grid_columnconfigure(1, weight=4) # צד ימין

        # # --- צד שמאל: רשימת הפינות (Checklist) ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="gray15")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=(0, 20), pady=20)
        
        # ctk.CTkLabel(self.sidebar, text="STATUS CHECK", font=ctk.CTkFont(size=20, weight="bold", underline=True)).pack(pady=20)
        
        # # יצירת המחוונים (נשמור אותם ברשימה כדי לגשת אליהם אח"כ)
        # self.corner_widgets = {} 
        
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=15, padx=10, fill="x")
            
            # # טקסט "Corner X"
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=18))
            # lbl.pack(side="left", padx=10)
            
            # # "נורה" שמציגה את הסטטוס (כפתור מנוטרל שמשמש כאינדיקטור)
            # indicator = ctk.CTkButton(frame, text="WAITING", width=80, height=30,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=10)
            
            # # שמירה במילון לפי מספר הפינה
            # self.corner_widgets[i] = indicator

        # # --- צד ימין: תצוגה ראשית ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.display_area, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack(pady=10)

        # # תצוגת התמונה - הוגדלה ל-1000x500
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="gray20", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.display_area, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_thread)
        # self.btn_start.pack(pady=10)

        # # סטטוס ובר התקדמות
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # פונקציות GUI
    # # ============================================================
    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # """מאפס את כל הנורות לאפור"""
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color="gray", text="WAITING")

    # def set_corner_status(self, corner_id, is_pass):
        # """עדכון צבע הנורה לפינה ספציפית"""
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if is_pass:
                # widget.configure(fg_color="green", text="PASS")
            # else:
                # widget.configure(fg_color="red", text="FAIL")

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    # def start_process_thread(self):
        # sn = self.entry_sn.get().strip()
        # if not sn:
            # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
            # return

        # self.btn_start.configure(state="disabled", text="RUNNING...")
        # self.entry_sn.configure(state="disabled")
        
        # # איפוס הויזואליזציה בצד
        # self.reset_indicators()
        
        # threading.Thread(target=self.run_logic, args=(sn,), daemon=True).start()

    # def run_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # # א. צילום
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # # ב. עיבוד
                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # # ג. עדכון תצוגה (תמונה + נורה בצד)
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # # עדכון הרשימה בצד שמאל!
                # self.after(0, lambda c=corner_id, ok=is_ok: self.set_corner_status(c, ok))

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # # ד. סיבוב
                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # # סיום
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))

    # # --- Helpers ---
    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # # גודל מתוקן: 1000x500
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


##########--------------------------------------------------------------------------#################

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading
# from tkinter import filedialog 

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.selected_file_path = None
        # self.mode_var = ctk.StringVar(value="Live Inspection")

        # # גריד ראשי לחלון
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(10, 5))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(280, 85))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי (שיטת 3 העמודות לאיזון)
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # self.main_frame.grid_columnconfigure(0, weight=0) 
        # self.main_frame.grid_columnconfigure(1, weight=1) 
        # self.main_frame.grid_columnconfigure(2, weight=0)

        # # --- 1. צד שמאל: התפריט הצף ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # self.sidebar.grid_propagate(False) 
        
        # ctk.CTkLabel(self.sidebar, text="STATUS CHECK", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(40, 20))
        
        # self.corner_widgets = {} 
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=15, padx=10, fill="x")
            
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=18))
            # lbl.pack(side="left", padx=10)
            
            # indicator = ctk.CTkButton(frame, text="WAITING", width=90, height=32,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=5)
            # self.corner_widgets[i] = indicator

        # # --- 2. צד ימין: ה"משקולת" לאיזון ---
        # self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        # self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # # --- 3. האמצע: התצוגה הראשית ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # בורר מצבים (Live / File)
        # self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  # values=["Live Inspection", "File Analysis"],
                                                  # command=self.on_mode_change,
                                                  # font=ctk.CTkFont(size=18, weight="bold"),
                                                  # width=400, height=40)
        # self.mode_switch.set("Live Inspection")
        # self.mode_switch.pack(pady=(10, 20))

        # self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.input_frame.pack(pady=10)

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack()

        # # כפתור בחירת קובץ (מוסתר בהתחלה)
        # self.btn_browse = ctk.CTkButton(self.input_frame, text="📂 Choose Image File", 
                                        # font=ctk.CTkFont(size=20), width=400, height=50,
                                        # fg_color="#444444", hover_color="#333333",
                                        # command=self.browse_file)

        # # תצוגת התמונה
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="#1a1a1a", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.display_area, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    # def on_mode_change(self, value):
        # self.mode_var.set(value)
        # if value == "Live Inspection":
            # self.btn_browse.pack_forget() 
            # self.entry_sn.pack()          
            # self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            # self.btn_start.configure(text="START INSPECTION")
            # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
            
        # else: # File Analysis
            # self.entry_sn.pack_forget()   
            # self.btn_browse.pack()        
            # self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            # self.btn_start.configure(text="ANALYZE IMAGE")
            # self.reset_indicators()

    # def browse_file(self):
        # # --- התיקון הסופי: ---
        # # 1. חיפוש ספציפי של PNG (אותיות גדולות)
        # # 2. הוספת "All files" כדי שתמיד תוכלי לראות הכל אם הפילטר נכשל
        # filename = filedialog.askopenfilename(
            # title="Select Image", 
            # filetypes=[
                # ("PNG Image", "*.PNG"),
                # ("png Image", "*.png"),  
                # ("All files", "*.*")
            # ]
        # )
        
        # if filename:
            # self.selected_file_path = filename
            # self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            # self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            # self.show_image_on_gui(filename)

    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color="gray", text="WAITING")

    # def set_corner_status(self, corner_id, is_pass):
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if is_pass:
                # widget.configure(fg_color="green", text="PASS")
            # else:
                # widget.configure(fg_color="#ff3333", text="FAIL")

    # def start_process_clicked(self):
        # mode = self.mode_var.get()
        
        # if mode == "Live Inspection":
            # sn = self.entry_sn.get().strip()
            # if not sn:
                # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="RUNNING...")
            # self.entry_sn.configure(state="disabled")
            # self.mode_switch.configure(state="disabled") 
            # self.reset_indicators()
            # threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        # else: # File Mode
            # if not self.selected_file_path:
                # self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="PROCESSING...")
            # threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # # --- לוגיקה לניתוח קובץ ---
    # def run_file_logic(self, file_path):
        # try:
            # self.update_progress(0.2)
            # self.update_status("Analyzing Image...", "yellow")
            # time.sleep(0.5) 

            # is_ok = yellow_algo.check_yellow_defect(file_path)
            # self.update_progress(0.8)

            # dir_name = os.path.dirname(file_path)
            # base_name = os.path.basename(file_path)
            # name_no_ext = os.path.splitext(base_name)[0]
            # result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            # self.show_image_on_gui(result_path)
            # self.update_progress(1.0)

            # if is_ok:
                # self.update_status("Result: PASS ✅", "green")
                # buzzer.beep_ok()
            # else:
                # self.update_status("Result: FAIL ❌", "red")
                # buzzer.beep_fail()

        # except Exception as e:
            # print(f"Error: {e}")
            # self.update_status("Analysis Error", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # # --- לוגיקה לבדיקה חיה ---
    # def run_live_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # self.after(0, lambda c=corner_id, ok=is_ok: self.set_corner_status(c, ok))

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))
            # self.after(0, lambda: self.mode_switch.configure(state="normal"))

    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


#####--------------------------------------------------------------------------------------------##############


# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading
# from tkinter import filedialog 

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.selected_file_path = None
        # self.mode_var = ctk.StringVar(value="Live Inspection")

        # # גריד ראשי לחלון
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(10, 5))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(280, 85))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי (שיטת 3 העמודות לאיזון)
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # self.main_frame.grid_columnconfigure(0, weight=0) 
        # self.main_frame.grid_columnconfigure(1, weight=1) 
        # self.main_frame.grid_columnconfigure(2, weight=0)

        # # --- 1. צד שמאל: התפריט הצף ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # self.sidebar.grid_propagate(False) 
        
        # # כותרת סטטוס פינות
        # ctk.CTkLabel(self.sidebar, text="CORNER CHECK", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(30, 15))
        
        # self.corner_widgets = {} 
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=10, padx=10, fill="x")
            
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=16))
            # lbl.pack(side="left", padx=10)
            
            # indicator = ctk.CTkButton(frame, text="WAITING", width=90, height=32,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=5)
            # self.corner_widgets[i] = indicator

        # # --- תוספת: קו מפריד וסטטוס כללי ---
        
        # # קו מפריד
        # ctk.CTkFrame(self.sidebar, height=2, fg_color="gray40").pack(fill="x", pady=20, padx=20)
        
        # # כותרת לתוצאה הסופית
        # ctk.CTkLabel(self.sidebar, text="COMPONENT STATUS", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 10))
        
        # # האינדיקטור הגדול למטה
        # self.total_status_indicator = ctk.CTkButton(self.sidebar, text="WAITING", width=200, height=50,
                                                    # fg_color="gray", state="disabled", 
                                                    # text_color_disabled="white",
                                                    # font=ctk.CTkFont(size=20, weight="bold"))
        # self.total_status_indicator.pack(pady=10)

        # # --- 2. צד ימין: ה"משקולת" לאיזון ---
        # self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        # self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # # --- 3. האמצע: התצוגה הראשית ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # בורר מצבים (Live / File)
        # self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  # values=["Live Inspection", "File Analysis"],
                                                  # command=self.on_mode_change,
                                                  # font=ctk.CTkFont(size=18, weight="bold"),
                                                  # width=400, height=40)
        # self.mode_switch.set("Live Inspection")
        # self.mode_switch.pack(pady=(10, 20))

        # self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.input_frame.pack(pady=10)

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack()

        # # כפתור בחירת קובץ
        # self.btn_browse = ctk.CTkButton(self.input_frame, text="📂 Choose Image File", 
                                        # font=ctk.CTkFont(size=20), width=400, height=50,
                                        # fg_color="#444444", hover_color="#333333",
                                        # command=self.browse_file)

        # # תצוגת התמונה
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="#1a1a1a", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.display_area, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    # def on_mode_change(self, value):
        # self.mode_var.set(value)
        # if value == "Live Inspection":
            # self.btn_browse.pack_forget() 
            # self.entry_sn.pack()          
            # self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            # self.btn_start.configure(text="START INSPECTION")
            # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
            
        # else: # File Analysis
            # self.entry_sn.pack_forget()   
            # self.btn_browse.pack()        
            # self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            # self.btn_start.configure(text="ANALYZE IMAGE")
            # self.reset_indicators()

    # def browse_file(self):
        # filename = filedialog.askopenfilename(
            # title="Select Image", 
            # filetypes=[
                # ("PNG Image", "*.PNG"),
                # ("png Image", "*.png"),  
                # ("All files", "*.*")
            # ]
        # )
        # if filename:
            # self.selected_file_path = filename
            # self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            # self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            # self.show_image_on_gui(filename)

    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # # איפוס הפינות
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color="gray", text="WAITING")
        # # איפוס הסטטוס הכללי
        # self.set_total_status("WAITING")

    # def set_corner_status(self, corner_id, is_pass):
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if is_pass:
                # widget.configure(fg_color="green", text="PASS")
            # else:
                # widget.configure(fg_color="#ff3333", text="FAIL")

    # def set_total_status(self, status):
        # """פונקציה לעדכון הסטטוס הכללי למטה"""
        # if status == "PASS":
            # self.total_status_indicator.configure(fg_color="green", text="PASS")
        # elif status == "FAIL":
            # self.total_status_indicator.configure(fg_color="#ff3333", text="FAIL")
        # else:
            # self.total_status_indicator.configure(fg_color="gray", text="WAITING")

    # def start_process_clicked(self):
        # mode = self.mode_var.get()
        
        # if mode == "Live Inspection":
            # sn = self.entry_sn.get().strip()
            # if not sn:
                # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="RUNNING...")
            # self.entry_sn.configure(state="disabled")
            # self.mode_switch.configure(state="disabled") 
            # self.reset_indicators()
            # threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        # else: # File Mode
            # if not self.selected_file_path:
                # self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="PROCESSING...")
            # threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # # --- לוגיקה לניתוח קובץ ---
    # def run_file_logic(self, file_path):
        # try:
            # self.update_progress(0.2)
            # self.update_status("Analyzing Image...", "yellow")
            # time.sleep(0.5) 

            # is_ok = yellow_algo.check_yellow_defect(file_path)
            # self.update_progress(0.8)

            # dir_name = os.path.dirname(file_path)
            # base_name = os.path.basename(file_path)
            # name_no_ext = os.path.splitext(base_name)[0]
            # result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            # self.show_image_on_gui(result_path)
            # self.update_progress(1.0)

            # if is_ok:
                # self.update_status("Result: PASS ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS")) # עדכון הסטטוס הכללי
                # buzzer.beep_ok()
            # else:
                # self.update_status("Result: FAIL ❌", "red")
                # self.after(0, lambda: self.set_total_status("FAIL")) # עדכון הסטטוס הכללי
                # buzzer.beep_fail()

        # except Exception as e:
            # print(f"Error: {e}")
            # self.update_status("Analysis Error", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # # --- לוגיקה לבדיקה חיה ---
    # def run_live_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # self.after(0, lambda c=corner_id, ok=is_ok: self.set_corner_status(c, ok))

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # # עדכון סופי של הסטטוס הכללי
            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
                # self.after(0, lambda: self.set_total_status("FAIL"))
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS"))

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))
            # self.after(0, lambda: self.mode_switch.configure(state="normal"))

    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


# #####-------------------- WORKS ... BUT RESET MISSING (WITHOUT "NEW SCAN" BUTTON) ... --------------------------------------########

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading
# from tkinter import filedialog 

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.selected_file_path = None
        # self.mode_var = ctk.StringVar(value="Live Inspection")

        # # גריד ראשי לחלון
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(10, 5))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(280, 85))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי (שיטת 3 העמודות לאיזון)
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # self.main_frame.grid_columnconfigure(0, weight=0) 
        # self.main_frame.grid_columnconfigure(1, weight=1) 
        # self.main_frame.grid_columnconfigure(2, weight=0)

        # # --- 1. צד שמאל: התפריט הצף ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # self.sidebar.grid_propagate(False) 
        
        # # כותרת סטטוס פינות
        # ctk.CTkLabel(self.sidebar, text="CORNER CHECK", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(30, 15))
        
        # self.corner_widgets = {} 
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=10, padx=10, fill="x")
            
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=16))
            # lbl.pack(side="left", padx=10)
            
            # indicator = ctk.CTkButton(frame, text="WAITING", width=90, height=32,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=5)
            # self.corner_widgets[i] = indicator

        # # --- תוספת: "קפיץ" (Spacer) שדוחף את הכל למטה ---
        # spacer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        # spacer.pack(fill="y", expand=True) # expand=True אומר לו לתפוס את כל המקום הריק

        # # קו מפריד
        # ctk.CTkFrame(self.sidebar, height=2, fg_color="gray40").pack(fill="x", pady=10, padx=20)
        
        # # כותרת לתוצאה הסופית
        # ctk.CTkLabel(self.sidebar, text="COMPONENT STATUS", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 5))
        
        # # האינדיקטור הגדול למטה (עם רווח מהרצפה)
        # self.total_status_indicator = ctk.CTkButton(self.sidebar, text="WAITING", width=200, height=50,
                                                    # fg_color="gray", state="disabled", 
                                                    # text_color_disabled="white",
                                                    # font=ctk.CTkFont(size=20, weight="bold"))
        # self.total_status_indicator.pack(pady=(5, 30)) # 30 פיקסלים רווח מלמטה

        # # --- 2. צד ימין: ה"משקולת" לאיזון ---
        # self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        # self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # # --- 3. האמצע: התצוגה הראשית ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # בורר מצבים (Live / File)
        # self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  # values=["Live Inspection", "File Analysis"],
                                                  # command=self.on_mode_change,
                                                  # font=ctk.CTkFont(size=18, weight="bold"),
                                                  # width=400, height=40)
        # self.mode_switch.set("Live Inspection")
        # self.mode_switch.pack(pady=(10, 20))

        # self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.input_frame.pack(pady=10)

        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", font=ctk.CTkFont(size=24),
                                     # width=400, height=50)
        # self.entry_sn.pack()

        # # כפתור בחירת קובץ
        # self.btn_browse = ctk.CTkButton(self.input_frame, text="Choose Image File", 
                                        # font=ctk.CTkFont(size=20), width=400, height=50,
                                        # fg_color="#444444", hover_color="#333333",
                                        # command=self.browse_file)

        # # תצוגת התמונה
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="#1a1a1a", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # כפתור התחלה
        # self.btn_start = ctk.CTkButton(self.display_area, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(pady=20)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    # def on_mode_change(self, value):
        # self.mode_var.set(value)
        # if value == "Live Inspection":
            # self.btn_browse.pack_forget() 
            # self.entry_sn.pack()          
            # self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            # self.btn_start.configure(text="START INSPECTION")
            # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
            
        # else: # File Analysis
            # self.entry_sn.pack_forget()   
            # self.btn_browse.pack()        
            # self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            # self.btn_start.configure(text="ANALYZE IMAGE")
            # self.reset_indicators()

    # def browse_file(self):
        # filename = filedialog.askopenfilename(
            # title="Select Image", 
            # filetypes=[
                # ("PNG Image", "*.PNG"),
                # ("png Image", "*.png"),  
                # ("All files", "*.*")
            # ]
        # )
        # if filename:
            # self.selected_file_path = filename
            # self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            # self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            # self.show_image_on_gui(filename)

    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # # איפוס הפינות
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color="gray", text="WAITING")
        # # איפוס הסטטוס הכללי
        # self.set_total_status("WAITING")

    # def set_corner_status(self, corner_id, is_pass):
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if is_pass:
                # widget.configure(fg_color="green", text="PASS")
            # else:
                # widget.configure(fg_color="#ff3333", text="FAIL")

    # def set_total_status(self, status):
        # """פונקציה לעדכון הסטטוס הכללי למטה"""
        # if status == "PASS":
            # self.total_status_indicator.configure(fg_color="green", text="PASS")
        # elif status == "FAIL":
            # self.total_status_indicator.configure(fg_color="#ff3333", text="FAIL")
        # else:
            # self.total_status_indicator.configure(fg_color="gray", text="WAITING")

    # def start_process_clicked(self):
        # mode = self.mode_var.get()
        
        # if mode == "Live Inspection":
            # sn = self.entry_sn.get().strip()
            # if not sn:
                # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="RUNNING...")
            # self.entry_sn.configure(state="disabled")
            # self.mode_switch.configure(state="disabled") 
            # self.reset_indicators()
            # threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        # else: # File Mode
            # if not self.selected_file_path:
                # self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="PROCESSING...")
            # threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # # --- לוגיקה לניתוח קובץ ---
    # def run_file_logic(self, file_path):
        # try:
            # self.update_progress(0.2)
            # self.update_status("Analyzing Image...", "yellow")
            # time.sleep(0.5) 

            # is_ok = yellow_algo.check_yellow_defect(file_path)
            # self.update_progress(0.8)

            # dir_name = os.path.dirname(file_path)
            # base_name = os.path.basename(file_path)
            # name_no_ext = os.path.splitext(base_name)[0]
            # result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            # self.show_image_on_gui(result_path)
            # self.update_progress(1.0)

            # if is_ok:
                # self.update_status("Result: PASS ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS")) # עדכון הסטטוס הכללי
                # buzzer.beep_ok()
            # else:
                # self.update_status("Result: FAIL ❌", "red")
                # self.after(0, lambda: self.set_total_status("FAIL")) # עדכון הסטטוס הכללי
                # buzzer.beep_fail()

        # except Exception as e:
            # print(f"Error: {e}")
            # self.update_status("Analysis Error", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # # --- לוגיקה לבדיקה חיה ---
    # def run_live_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # self.after(0, lambda c=corner_id, ok=is_ok: self.set_corner_status(c, ok))

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # # עדכון סופי של הסטטוס הכללי
            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
                # self.after(0, lambda: self.set_total_status("FAIL"))
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS"))

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))
            # self.after(0, lambda: self.mode_switch.configure(state="normal"))

    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


##-----------------------FINAL - WITH "NEW SCAN" BUTTON !!---------##############################

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading
# from tkinter import filedialog 

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.selected_file_path = None
        # self.mode_var = ctk.StringVar(value="Live Inspection")

        # # גריד ראשי לחלון
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(10, 5))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(280, 85))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי (שיטת 3 העמודות לאיזון)
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # self.main_frame.grid_columnconfigure(0, weight=0) 
        # self.main_frame.grid_columnconfigure(1, weight=1) 
        # self.main_frame.grid_columnconfigure(2, weight=0)

        # # --- 1. צד שמאל: התפריט הצף ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # self.sidebar.grid_propagate(False) 
        
        # ctk.CTkLabel(self.sidebar, text="CORNER CHECK", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(30, 15))
        
        # self.corner_widgets = {} 
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=10, padx=10, fill="x")
            
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=16))
            # lbl.pack(side="left", padx=10)
            
            # indicator = ctk.CTkButton(frame, text="WAITING", width=90, height=32,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=5)
            # self.corner_widgets[i] = indicator

        # # קפיץ וסטטוס כללי
        # spacer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        # spacer.pack(fill="y", expand=True) 

        # ctk.CTkFrame(self.sidebar, height=2, fg_color="gray40").pack(fill="x", pady=10, padx=20)
        # ctk.CTkLabel(self.sidebar, text="COMPONENT STATUS", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 5))
        
        # self.total_status_indicator = ctk.CTkButton(self.sidebar, text="WAITING", width=200, height=50,
                                                    # fg_color="gray", state="disabled", 
                                                    # text_color_disabled="white",
                                                    # font=ctk.CTkFont(size=20, weight="bold"))
        # self.total_status_indicator.pack(pady=(5, 30)) 

        # # --- 2. צד ימין: משקולת לאיזון ---
        # self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        # self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # # --- 3. האמצע ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # בורר מצבים
        # self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  # values=["Live Inspection", "File Analysis"],
                                                  # command=self.on_mode_change,
                                                  # font=ctk.CTkFont(size=18, weight="bold"),
                                                  # width=400, height=40)
        # self.mode_switch.set("Live Inspection")
        # self.mode_switch.pack(pady=(10, 20))

        # self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.input_frame.pack(pady=10)

        # # --- תיקון זהות הטקסט ---
        # COMMON_FG = "#343638"      
        # COMMON_BORDER = "#565b5e"
        # # יצרנו פונט משותף לא מודגש
        # SHARED_FONT = ctk.CTkFont(size=22, weight="normal") 
        # # צבע אפור שמתאים ל-Placeholder
        # TEXT_COLOR = "#aab0b5" 
        
        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", 
                                     # font=SHARED_FONT,              # פונט אחיד
                                     # placeholder_text_color=TEXT_COLOR, # צבע אחיד
                                     # width=400, height=50,
                                     # corner_radius=6, 
                                     # fg_color=COMMON_FG, 
                                     # border_color=COMMON_BORDER, 
                                     # border_width=2)
        # self.entry_sn.pack()

        # # כפתור קובץ
        # self.btn_browse = ctk.CTkButton(self.input_frame, text="📂 Choose Image File", 
                                        # font=SHARED_FONT,           # פונט אחיד
                                        # text_color=TEXT_COLOR,      # צבע אחיד
                                        # width=400, height=50,
                                        # corner_radius=6, 
                                        # fg_color=COMMON_FG, 
                                        # border_color=COMMON_BORDER,
                                        # border_width=2,
                                        # hover_color="#3e4042",
                                        # command=self.browse_file)

        # # תצוגת התמונה
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="#1a1a1a", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # מסגרת כפתורים
        # self.buttons_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.buttons_frame.pack(pady=20)

        # self.btn_start = ctk.CTkButton(self.buttons_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(side="top", pady=5)

        # self.btn_reset = ctk.CTkButton(self.buttons_frame, 
                                       # text="NEW SCAN ⟳", 
                                       # font=ctk.CTkFont(size=18, weight="bold"),
                                       # width=200, height=40,
                                       # fg_color="#555555", hover_color="#333333",
                                       # command=self.reset_gui)
        # self.btn_reset.pack(side="top", pady=10)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    
    # def reset_gui(self):
        # """איפוס המסך והכנה לבדיקה חדשה"""
        # self.entry_sn.configure(state="normal")
        # self.entry_sn.delete(0, 'end')
        # self.entry_sn.configure(placeholder_text="Enter Serial Number")
        # self.focus() 
        
        # self.mode_switch.configure(state="normal")
        # self.selected_file_path = None
        # self.btn_browse.configure(text="Choose Image File")
        # self.image_display.configure(image=None, text="Waiting for scan...")
        
        # self.progress_bar.set(0)
        # self.status_label.configure(text="System Ready", text_color="white")
        # self.reset_indicators()
        
        # self.refresh_input_visibility()
        
        # self.btn_start.configure(state="normal", text="START INSPECTION" if self.mode_var.get() == "Live Inspection" else "ANALYZE IMAGE")

    # def refresh_input_visibility(self):
        # mode = self.mode_var.get()
        # self.btn_browse.pack_forget()
        # self.entry_sn.pack_forget()
        
        # if mode == "Live Inspection":
            # self.entry_sn.pack() 
            # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # else:
            # self.btn_browse.pack() 

    # def on_mode_change(self, value):
        # self.mode_var.set(value)
        # self.reset_gui() 
        
        # if value == "Live Inspection":
            # self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            # self.btn_start.configure(text="START INSPECTION")
        # else: 
            # self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            # self.btn_start.configure(text="ANALYZE IMAGE")

    # def browse_file(self):
        # filename = filedialog.askopenfilename(
            # title="Select Image", 
            # filetypes=[
                # ("PNG Image", "*.PNG"),
                # ("png Image", "*.png"),  
                # ("All files", "*.*")
            # ]
        # )
        # if filename:
            # self.selected_file_path = filename
            # self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            # self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            # self.show_image_on_gui(filename)

    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color="gray", text="WAITING")
        # self.set_total_status("WAITING")

    # def set_corner_status(self, corner_id, is_pass):
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if is_pass:
                # widget.configure(fg_color="green", text="PASS")
            # else:
                # widget.configure(fg_color="#ff3333", text="FAIL")

    # def set_total_status(self, status):
        # if status == "PASS":
            # self.total_status_indicator.configure(fg_color="green", text="PASS")
        # elif status == "FAIL":
            # self.total_status_indicator.configure(fg_color="#ff3333", text="FAIL")
        # else:
            # self.total_status_indicator.configure(fg_color="gray", text="WAITING")

    # def start_process_clicked(self):
        # mode = self.mode_var.get()
        
        # if mode == "Live Inspection":
            # sn = self.entry_sn.get().strip()
            # if not sn:
                # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="RUNNING...")
            # self.entry_sn.configure(state="disabled")
            # self.mode_switch.configure(state="disabled") 
            # self.reset_indicators()
            # threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        # else: # File Mode
            # if not self.selected_file_path:
                # self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="PROCESSING...")
            # threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # # --- לוגיקה לניתוח קובץ ---
    # def run_file_logic(self, file_path):
        # try:
            # self.update_progress(0.2)
            # self.update_status("Analyzing Image...", "yellow")
            # time.sleep(0.5) 

            # is_ok = yellow_algo.check_yellow_defect(file_path)
            # self.update_progress(0.8)

            # dir_name = os.path.dirname(file_path)
            # base_name = os.path.basename(file_path)
            # name_no_ext = os.path.splitext(base_name)[0]
            # result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            # self.show_image_on_gui(result_path)
            # self.update_progress(1.0)

            # if is_ok:
                # self.update_status("Result: PASS ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS")) 
                # buzzer.beep_ok()
            # else:
                # self.update_status("Result: FAIL ❌", "red")
                # self.after(0, lambda: self.set_total_status("FAIL")) 
                # buzzer.beep_fail()

        # except Exception as e:
            # print(f"Error: {e}")
            # self.update_status("Analysis Error", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # # --- לוגיקה לבדיקה חיה ---
    # def run_live_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # defect_found = False

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break

                # is_ok = yellow_algo.check_yellow_defect(filename)
                
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # self.after(0, lambda c=corner_id, ok=is_ok: self.set_corner_status(c, ok))

                # if not is_ok:
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # defect_found = True
                    # break 
                # else:
                    # buzzer.beep_ok()

                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # if defect_found:
                # self.update_status(f"SN: {serial_number} - FAILED", "red")
                # self.after(0, lambda: self.set_total_status("FAIL"))
            # else:
                # self.update_status(f"SN: {serial_number} - PASSED ✅", "green")
                # self.after(0, lambda: self.set_total_status("PASS"))

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))
            # self.after(0, lambda: self.mode_switch.configure(state="normal"))

    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()


# ##########    NEW FOR CHECK - WITH CLASS B - YELLOW ---------------------------###########

# import customtkinter as ctk
# from PIL import Image
# import os
# import sys
# import time
# import threading
# from tkinter import filedialog 

# # --- ייבוא החומרה והאלגוריתם ---
# try:
    # import hardware.camera as cam
    # import hardware.motor as motor
    # import hardware.buzzer as buzzer
    # import vision.yellow_check as yellow_algo
# except ImportError as e:
    # print(f"Error importing modules: {e}")

# # --- הגדרות ---
# RESULTS_BASE_FOLDER = "Test_Results"
# NUM_CORNERS = 4

# # צבעים לסטטוסים
# COLOR_PASS = "#008000"   # ירוק
# COLOR_WARN = "#ff9100"   # כתום/צהוב עבור Class B
# COLOR_FAIL = "#ff3333"   # אדום
# COLOR_WAIT = "gray"

# ctk.set_widget_scaling(1.0)
# ctk.set_appearance_mode("Dark")
# ctk.set_default_color_theme("blue")

# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()

        # # 1. הגדרות חלון
        # self.title("Philips - PDA Chipping Inspection")
        # self.attributes('-fullscreen', True)
        # self.after(500, lambda: self.attributes('-fullscreen', True))
        # self.bind("<Escape>", lambda event: self.close_app())

        # self.selected_file_path = None
        # self.mode_var = ctk.StringVar(value="Live Inspection")

        # # גריד ראשי לחלון
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=1)

        # # ============================================================
        # # כפתורי שליטה עליונים
        # # ============================================================
        # self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      # fg_color="#ff4444", hover_color="#cc0000",
                                      # font=ctk.CTkFont(size=18, weight="bold"),
                                      # command=self.close_app)
        # self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        # self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        # fg_color="#555555", hover_color="#333333",
                                        # font=ctk.CTkFont(size=18, weight="bold"),
                                        # command=self.toggle_fullscreen)
        # self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        # self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          # fg_color="#555555", hover_color="#333333",
                                          # font=ctk.CTkFont(size=18, weight="bold"),
                                          # command=self.minimize_app)
        # self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # # ============================================================
        # # חלק א': כותרת ולוגו
        # # ============================================================
        # self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.header_frame.grid(row=0, column=0, pady=(10, 5))

        # image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        # try:
            # self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           # dark_image=Image.open(image_path),
                                           # size=(280, 85))
            # self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            # self.label_logo.pack(side="top", pady=5)
        # except:
            # pass

        # self.label_title = ctk.CTkLabel(self.header_frame, 
                                        # text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        # font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        # self.label_title.pack(side="top")

        # # ============================================================
        # # חלק ב': האזור הראשי
        # # ============================================================
        # self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # self.main_frame.grid_columnconfigure(0, weight=0) 
        # self.main_frame.grid_columnconfigure(1, weight=1) 
        # self.main_frame.grid_columnconfigure(2, weight=0)

        # # --- 1. צד שמאל: התפריט הצף ---
        # self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # self.sidebar.grid_propagate(False) 
        
        # ctk.CTkLabel(self.sidebar, text="CORNER CHECK", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(30, 15))
        
        # self.corner_widgets = {} 
        # for i in range(1, NUM_CORNERS + 1):
            # frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            # frame.pack(pady=10, padx=10, fill="x")
            
            # lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=16))
            # lbl.pack(side="left", padx=10)
            
            # # רוחב הכפתור הוגדל מעט כדי להכיל "CLASS A"
            # indicator = ctk.CTkButton(frame, text="WAITING", width=100, height=32,
                                      # fg_color="gray", state="disabled", text_color_disabled="white")
            # indicator.pack(side="right", padx=5)
            # self.corner_widgets[i] = indicator

        # # קפיץ וסטטוס כללי
        # spacer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        # spacer.pack(fill="y", expand=True) 

        # ctk.CTkFrame(self.sidebar, height=2, fg_color="gray40").pack(fill="x", pady=10, padx=20)
        # ctk.CTkLabel(self.sidebar, text="COMPONENT STATUS", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 5))
        
        # self.total_status_indicator = ctk.CTkButton(self.sidebar, text="WAITING", width=200, height=50,
                                                    # fg_color="gray", state="disabled", 
                                                    # text_color_disabled="white",
                                                    # font=ctk.CTkFont(size=20, weight="bold"))
        # self.total_status_indicator.pack(pady=(5, 30)) 

        # # --- 2. צד ימין: משקולת לאיזון ---
        # self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        # self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # # --- 3. האמצע ---
        # self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        # self.display_area.grid(row=0, column=1, sticky="nsew")

        # # בורר מצבים
        # self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  # values=["Live Inspection", "File Analysis"],
                                                  # command=self.on_mode_change,
                                                  # font=ctk.CTkFont(size=18, weight="bold"),
                                                  # width=400, height=40)
        # self.mode_switch.set("Live Inspection")
        # self.mode_switch.pack(pady=(10, 20))

        # self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.input_frame.pack(pady=10)

        # COMMON_FG = "#343638"      
        # COMMON_BORDER = "#565b5e"
        # SHARED_FONT = ctk.CTkFont(size=22, weight="normal") 
        # TEXT_COLOR = "#aab0b5" 
        
        # # שדה SN
        # self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     # placeholder_text="Scan / Enter Serial Number", 
                                     # justify="center", 
                                     # font=SHARED_FONT,              
                                     # placeholder_text_color=TEXT_COLOR,
                                     # width=400, height=50,
                                     # corner_radius=6, 
                                     # fg_color=COMMON_FG, 
                                     # border_color=COMMON_BORDER, 
                                     # border_width=2)
        # self.entry_sn.pack()

        # # כפתור קובץ
        # self.btn_browse = ctk.CTkButton(self.input_frame, text=" Choose Image File", 
                                        # font=SHARED_FONT,           
                                        # text_color=TEXT_COLOR,      
                                        # width=400, height=50,
                                        # corner_radius=6, 
                                        # fg_color=COMMON_FG, 
                                        # border_color=COMMON_BORDER,
                                        # border_width=2,
                                        # hover_color="#3e4042",
                                        # command=self.browse_file)

        # # תצוגת התמונה
        # self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          # width=1000, height=500, 
                                          # fg_color="#1a1a1a", corner_radius=10)
        # self.image_display.pack(pady=10)

        # # מסגרת כפתורים
        # self.buttons_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        # self.buttons_frame.pack(pady=20)

        # self.btn_start = ctk.CTkButton(self.buttons_frame, 
                                       # text="START INSPECTION", 
                                       # font=ctk.CTkFont(size=24, weight="bold"),
                                       # width=300, height=60,
                                       # fg_color="#0066cc", hover_color="#004c99",
                                       # command=self.start_process_clicked)
        # self.btn_start.pack(side="top", pady=5)

        # self.btn_reset = ctk.CTkButton(self.buttons_frame, 
                                       # text="NEW SCAN ⟳", 
                                       # font=ctk.CTkFont(size=18, weight="bold"),
                                       # width=200, height=40,
                                       # fg_color="#555555", hover_color="#333333",
                                       # command=self.reset_gui)
        # self.btn_reset.pack(side="top", pady=10)

        # # סטטוס
        # self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         # font=ctk.CTkFont(size=24))
        # self.status_label.pack(pady=5)

        # self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        # self.progress_bar.set(0)
        # self.progress_bar.pack(pady=10)

    # # ============================================================
    # # לוגיקה
    # # ============================================================
    
    # def reset_gui(self):
        # self.entry_sn.configure(state="normal")
        # self.entry_sn.delete(0, 'end')
        # self.entry_sn.configure(placeholder_text="Enter Serial Number")
        # self.focus() 
        
        # self.mode_switch.configure(state="normal")
        # self.selected_file_path = None
        # self.btn_browse.configure(text="Choose Image File")
        # self.image_display.configure(image=None, text="Waiting for scan...")
        
        # self.progress_bar.set(0)
        # self.status_label.configure(text="System Ready", text_color="white")
        # self.reset_indicators()
        
        # self.refresh_input_visibility()
        
        # self.btn_start.configure(state="normal", text="START INSPECTION" if self.mode_var.get() == "Live Inspection" else "ANALYZE IMAGE")

    # def refresh_input_visibility(self):
        # mode = self.mode_var.get()
        # self.btn_browse.pack_forget()
        # self.entry_sn.pack_forget()
        
        # if mode == "Live Inspection":
            # self.entry_sn.pack() 
            # self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        # else:
            # self.btn_browse.pack() 

    # def on_mode_change(self, value):
        # self.mode_var.set(value)
        # self.reset_gui() 
        
        # if value == "Live Inspection":
            # self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            # self.btn_start.configure(text="START INSPECTION")
        # else: 
            # self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            # self.btn_start.configure(text="ANALYZE IMAGE")

    # def browse_file(self):
        # filename = filedialog.askopenfilename(
            # title="Select Image", 
            # filetypes=[
                # ("PNG Image", "*.PNG"),
                # ("png Image", "*.png"),  
                # ("All files", "*.*")
            # ]
        # )
        # if filename:
            # self.selected_file_path = filename
            # self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            # self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            # self.show_image_on_gui(filename)

    # def minimize_app(self):
        # self.iconify()

    # def toggle_fullscreen(self):
        # current_state = self.attributes('-fullscreen')
        # self.attributes('-fullscreen', not current_state)

    # def close_app(self):
        # try:
            # motor.finish_cycle()
        # except:
            # pass
        # self.destroy()
        # sys.exit()

    # def reset_indicators(self):
        # for i in range(1, NUM_CORNERS + 1):
            # self.corner_widgets[i].configure(fg_color=COLOR_WAIT, text="WAITING")
        # self.set_total_status("WAITING")

    # # --- עדכון: פונקציה שמקבלת סטטוס טקסטואלי ---
    # def set_corner_status(self, corner_id, status_text):
        # widget = self.corner_widgets.get(corner_id)
        # if widget:
            # if status_text == "CLASS A":
                # widget.configure(fg_color=COLOR_PASS, text="PASS")
            # elif status_text == "CLASS B":
                # widget.configure(fg_color=COLOR_WARN, text="WARNING")
            # elif status_text == "FAIL":
                # widget.configure(fg_color=COLOR_FAIL, text="FAIL")
            # else:
                # widget.configure(fg_color=COLOR_WAIT, text="WAITING")

    # def set_total_status(self, status):
        # if status == "CLASS A":
            # self.total_status_indicator.configure(fg_color=COLOR_PASS, text="CLASS A")
        # elif status == "CLASS B":
            # self.total_status_indicator.configure(fg_color=COLOR_WARN, text="CLASS B")
        # elif status == "FAIL":
            # self.total_status_indicator.configure(fg_color=COLOR_FAIL, text="FAIL")
        # else:
            # self.total_status_indicator.configure(fg_color=COLOR_WAIT, text="WAITING")

    # def start_process_clicked(self):
        # mode = self.mode_var.get()
        
        # if mode == "Live Inspection":
            # sn = self.entry_sn.get().strip()
            # if not sn:
                # self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="RUNNING...")
            # self.entry_sn.configure(state="disabled")
            # self.mode_switch.configure(state="disabled") 
            # self.reset_indicators()
            # threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        # else: # File Mode
            # if not self.selected_file_path:
                # self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                # return
            
            # self.btn_start.configure(state="disabled", text="PROCESSING...")
            # threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # # --- לוגיקה לניתוח קובץ ---
    # def run_file_logic(self, file_path):
        # try:
            # self.update_progress(0.2)
            # self.update_status("Analyzing Image...", "yellow")
            # time.sleep(0.5) 

            # # הציפייה היא שהפונקציה תחזיר מחרוזת: "CLASS A", "CLASS B" או "FAIL"
            # status_result = yellow_algo.check_yellow_defect(file_path)
            # self.update_progress(0.8)

            # dir_name = os.path.dirname(file_path)
            # base_name = os.path.basename(file_path)
            # name_no_ext = os.path.splitext(base_name)[0]
            # result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            # self.show_image_on_gui(result_path)
            # self.update_progress(1.0)

            # # טיפול בסטטוס
            # if status_result == "FAIL":
                # self.update_status(f"Result: {status_result} ❌", "red")
                # self.after(0, lambda: self.set_total_status("FAIL"))
                # buzzer.beep_fail()
            # else:
                # # גם CLASS A וגם CLASS B הם עוברים
                # icon = "✅" if status_result == "CLASS A" else "⚠️"
                # color = "green" if status_result == "CLASS A" else "orange"
                
                # self.update_status(f"Result: {status_result} {icon}", color)
                # self.after(0, lambda: self.set_total_status(status_result)) 
                # buzzer.beep_ok()

        # except Exception as e:
            # print(f"Error: {e}")
            # self.update_status("Analysis Error", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # # --- לוגיקה לבדיקה חיה ---
    # def run_live_logic(self, serial_number):
        # try:
            # self.update_status("Initializing Motor & Camera...", "yellow")
            # motor.reset_sequence()
            
            # component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            # if not os.path.exists(component_folder):
                # os.makedirs(component_folder)

            # # משתנה למעקב אחרי הסטטוס הכי גרוע שנמצא
            # # סדר חומרה: CLASS A (הכי טוב) -> CLASS B -> FAIL (הכי גרוע)
            # final_component_status = "CLASS A"

            # for i in range(NUM_CORNERS):
                # corner_id = i + 1
                # progress_val = i / NUM_CORNERS
                # self.update_progress(progress_val)
                # self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                # filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                # if not cam.take_picture(filename):
                    # self.update_status("Camera Error!", "red")
                    # buzzer.beep_fail()
                    # final_component_status = "FAIL"
                    # break

                # # קריאה לאלגוריתם - מחזיר מחרוזת
                # status_result = yellow_algo.check_yellow_defect(filename)
                
                # result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                # self.show_image_on_gui(result_img_path)
                
                # # עדכון המחוון של הפינה הספציפית
                # self.after(0, lambda c=corner_id, s=status_result: self.set_corner_status(c, s))

                # if status_result == "FAIL":
                    # self.update_status(f"Defect at Corner {corner_id}!", "red")
                    # buzzer.beep_fail()
                    # final_component_status = "FAIL"
                    # break # עוצרים בכישלון
                
                # elif status_result == "CLASS B":
                    # # שומרים שיש שבר קטן, אבל ממשיכים לבדוק
                    # if final_component_status == "CLASS A":
                        # final_component_status = "CLASS B"
                    # buzzer.beep_ok()

                # else: # CLASS A
                    # buzzer.beep_ok()

                # if i < NUM_CORNERS - 1:
                    # self.update_status(f"Rotating to next corner...", "cyan")
                    # motor.rotate_to_next_corner()
            
            # self.update_progress(1.0)
            # self.update_status("Returning to Start Position...", "orange")
            # time.sleep(0.5)
            # motor.finish_cycle() 

            # # סיכום סופי
            # if final_component_status == "FAIL":
                # self.update_status(f"SN: {serial_number} - FAILED ❌", "red")
            # elif final_component_status == "CLASS B":
                # self.update_status(f"SN: {serial_number} - CLASS B ⚠️", "orange")
            # else:
                # self.update_status(f"SN: {serial_number} - CLASS A ✅", "green")
                
            # self.after(0, lambda: self.set_total_status(final_component_status))

        # except Exception as e:
            # print(f"CRITICAL ERROR: {e}")
            # self.update_status("System Error!", "red")
        
        # finally:
            # self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            # self.after(0, lambda: self.entry_sn.configure(state="normal"))
            # self.after(0, lambda: self.mode_switch.configure(state="normal"))

    # def update_status(self, text, color="white"):
        # self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    # def update_progress(self, val):
        # self.after(0, lambda: self.progress_bar.set(val))

    # def show_image_on_gui(self, img_path):
        # if os.path.exists(img_path):
            # try:
                # pil_img = Image.open(img_path)
                # ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                # self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            # except Exception as e:
                # print(f"Error showing image: {e}")

# if __name__ == "__main__":
    # app = App()
    # app.mainloop()
    

########--------------FINAL - WITH CLASS A, CLASS B AND FAIL - WITH COMMENTS IN ENGLISH --------########

import customtkinter as ctk
from PIL import Image
import os
import sys
import time
import threading
from tkinter import filedialog 

# --- Hardware and Algorithm Imports ---
try:
    import hardware.camera as cam
    import hardware.motor as motor
    import hardware.buzzer as buzzer
    import vision.yellow_check as yellow_algo
except ImportError as e:
    print(f"Error importing modules: {e}")

# --- Configuration ---
RESULTS_BASE_FOLDER = "Test_Results"
NUM_CORNERS = 4

# Status Colors
COLOR_PASS = "#008000"   # Green
COLOR_WARN = "#ff9100"   # Orange-Yellow for Class B
COLOR_FAIL = "#ff3333"   # Red
COLOR_WAIT = "gray"

ctk.set_widget_scaling(1.0)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Window Configuration
        self.title("Philips - PDA Chipping Inspection")
        self.attributes('-fullscreen', True)
        self.after(500, lambda: self.attributes('-fullscreen', True))
        self.bind("<Escape>", lambda event: self.close_app())

        self.selected_file_path = None
        self.mode_var = ctk.StringVar(value="Live Inspection")

        # Main Window Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ============================================================
        # Top Control Buttons
        # ============================================================
        self.btn_exit = ctk.CTkButton(self, text="✕", width=50, height=40,
                                      fg_color="#ff4444", hover_color="#cc0000",
                                      font=ctk.CTkFont(size=18, weight="bold"),
                                      command=self.close_app)
        self.btn_exit.place(relx=0.99, rely=0.01, anchor="ne")

        self.btn_resize = ctk.CTkButton(self, text="❐", width=50, height=40,
                                        fg_color="#555555", hover_color="#333333",
                                        font=ctk.CTkFont(size=18, weight="bold"),
                                        command=self.toggle_fullscreen)
        self.btn_resize.place(relx=0.94, rely=0.01, anchor="ne")

        self.btn_minimize = ctk.CTkButton(self, text="—", width=50, height=40,
                                          fg_color="#555555", hover_color="#333333",
                                          font=ctk.CTkFont(size=18, weight="bold"),
                                          command=self.minimize_app)
        self.btn_minimize.place(relx=0.89, rely=0.01, anchor="ne")

        # ============================================================
        # Part A: Header and Logo
        # ============================================================
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=(10, 5))

        image_path = os.path.join(os.path.dirname(__file__), "philips_logo.PNG")
        try:
            self.logo_image = ctk.CTkImage(light_image=Image.open(image_path),
                                           dark_image=Image.open(image_path),
                                           size=(280, 85))
            self.label_logo = ctk.CTkLabel(self.header_frame, text="", image=self.logo_image)
            self.label_logo.pack(side="top", pady=5)
        except:
            pass

        self.label_title = ctk.CTkLabel(self.header_frame, 
                                        text="PDA CHIPPING IDENTIFICATION SYSTEM", 
                                        font=ctk.CTkFont(family="Arial", size=26, weight="bold"))
        self.label_title.pack(side="top")

        # ============================================================
        # Part B: Main Area
        # ============================================================
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        self.main_frame.grid_columnconfigure(0, weight=0) 
        self.main_frame.grid_columnconfigure(1, weight=1) 
        self.main_frame.grid_columnconfigure(2, weight=0)

        # --- 1. Left Side: Floating Sidebar ---
        self.sidebar = ctk.CTkFrame(self.main_frame, width=280, corner_radius=20, fg_color="#2b2b2b")
        self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        self.sidebar.grid_propagate(False) 
        
        ctk.CTkLabel(self.sidebar, text="CORNER CHECK", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(30, 15))
        
        self.corner_widgets = {} 
        for i in range(1, NUM_CORNERS + 1):
            frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
            frame.pack(pady=10, padx=10, fill="x")
            
            lbl = ctk.CTkLabel(frame, text=f"Corner {i}:", font=ctk.CTkFont(size=16))
            lbl.pack(side="left", padx=10)
            
            # Button width increased slightly to fit "CLASS A"
            indicator = ctk.CTkButton(frame, text="WAITING", width=100, height=32,
                                      fg_color="gray", state="disabled", text_color_disabled="white")
            indicator.pack(side="right", padx=5)
            self.corner_widgets[i] = indicator

        # Spacer and General Status
        spacer = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        spacer.pack(fill="y", expand=True) 

        ctk.CTkFrame(self.sidebar, height=2, fg_color="gray40").pack(fill="x", pady=10, padx=20)
        ctk.CTkLabel(self.sidebar, text="COMPONENT STATUS", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(0, 5))
        
        self.total_status_indicator = ctk.CTkButton(self.sidebar, text="WAITING", width=200, height=50,
                                                    fg_color="gray", state="disabled", 
                                                    text_color_disabled="white",
                                                    font=ctk.CTkFont(size=20, weight="bold"))
        self.total_status_indicator.pack(pady=(5, 30)) 

        # --- 2. Right Side: Balance Weight ---
        self.right_balance = ctk.CTkFrame(self.main_frame, width=280, fg_color="transparent")
        self.right_balance.grid(row=0, column=2, sticky="ns", padx=25, pady=25)

        # --- 3. Center Area ---
        self.display_area = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.display_area.grid(row=0, column=1, sticky="nsew")

        # Mode Selector
        self.mode_switch = ctk.CTkSegmentedButton(self.display_area, 
                                                  values=["Live Inspection", "File Analysis"],
                                                  command=self.on_mode_change,
                                                  font=ctk.CTkFont(size=18, weight="bold"),
                                                  width=400, height=40)
        self.mode_switch.set("Live Inspection")
        self.mode_switch.pack(pady=(10, 20))

        self.input_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        self.input_frame.pack(pady=10)

        COMMON_FG = "#343638"       
        COMMON_BORDER = "#565b5e"
        SHARED_FONT = ctk.CTkFont(size=22, weight="normal") 
        TEXT_COLOR = "#aab0b5" 
        
        # SN Field
        self.entry_sn = ctk.CTkEntry(self.input_frame, 
                                     placeholder_text="Enter Serial Number", 
                                     justify="center", 
                                     font=SHARED_FONT,                   
                                     placeholder_text_color=TEXT_COLOR,
                                     width=400, height=50,
                                     corner_radius=6, 
                                     fg_color=COMMON_FG, 
                                     border_color=COMMON_BORDER, 
                                     border_width=2)
        self.entry_sn.pack()

        # File Button
        self.btn_browse = ctk.CTkButton(self.input_frame, text="Choose Image File", 
                                        font=SHARED_FONT,            
                                        text_color=TEXT_COLOR,       
                                        width=400, height=50,
                                        corner_radius=6, 
                                        fg_color=COMMON_FG, 
                                        border_color=COMMON_BORDER,
                                        border_width=2,
                                        hover_color="#3e4042",
                                        command=self.browse_file)

        # Image Display
        self.image_display = ctk.CTkLabel(self.display_area, text="Waiting for scan...", 
                                          width=1000, height=500, 
                                          fg_color="#1a1a1a", corner_radius=10)
        self.image_display.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = ctk.CTkFrame(self.display_area, fg_color="transparent")
        self.buttons_frame.pack(pady=20)

        self.btn_start = ctk.CTkButton(self.buttons_frame, 
                                       text="START INSPECTION", 
                                       font=ctk.CTkFont(size=24, weight="bold"),
                                       width=300, height=60,
                                       fg_color="#0066cc", hover_color="#004c99",
                                       command=self.start_process_clicked)
        self.btn_start.pack(side="top", pady=5)

        self.btn_reset = ctk.CTkButton(self.buttons_frame, 
                                       text="NEW SCAN ⟳", 
                                       font=ctk.CTkFont(size=18, weight="bold"),
                                       width=200, height=40,
                                       fg_color="#555555", hover_color="#333333",
                                       command=self.reset_gui)
        self.btn_reset.pack(side="top", pady=10)

        # Status
        self.status_label = ctk.CTkLabel(self.display_area, text="System Ready", 
                                         font=ctk.CTkFont(size=24))
        self.status_label.pack(pady=5)

        self.progress_bar = ctk.CTkProgressBar(self.display_area, width=800, height=20)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

    # ============================================================
    # Logic
    # ============================================================
    
    def reset_gui(self):
        self.entry_sn.configure(state="normal")
        self.entry_sn.delete(0, 'end')
        self.entry_sn.configure(placeholder_text="Enter Serial Number")
        self.focus() 
        
        self.mode_switch.configure(state="normal")
        self.selected_file_path = None
        self.btn_browse.configure(text="Choose Image File")
        self.image_display.configure(image=None, text="Waiting for scan...")
        
        self.progress_bar.set(0)
        self.status_label.configure(text="System Ready", text_color="white")
        self.reset_indicators()
        
        self.refresh_input_visibility()
        
        self.btn_start.configure(state="normal", text="START INSPECTION" if self.mode_var.get() == "Live Inspection" else "ANALYZE IMAGE")

    def refresh_input_visibility(self):
        mode = self.mode_var.get()
        self.btn_browse.pack_forget()
        self.entry_sn.pack_forget()
        
        if mode == "Live Inspection":
            self.entry_sn.pack() 
            self.sidebar.grid(row=0, column=0, sticky="ns", padx=25, pady=25)
        else:
            self.btn_browse.pack() 

    def on_mode_change(self, value):
        self.mode_var.set(value)
        self.reset_gui() 
        
        if value == "Live Inspection":
            self.status_label.configure(text="System Ready (Live Mode)", text_color="white")
            self.btn_start.configure(text="START INSPECTION")
        else: 
            self.status_label.configure(text="Select an image file to analyze", text_color="cyan")
            self.btn_start.configure(text="ANALYZE IMAGE")

    def browse_file(self):
        filename = filedialog.askopenfilename(
            title="Select Image", 
            filetypes=[
                ("PNG Image", "*.PNG"),
                ("png Image", "*.png"),  
                ("All files", "*.*")
            ]
        )
        if filename:
            self.selected_file_path = filename
            self.btn_browse.configure(text=f"File: {os.path.basename(filename)}")
            self.status_label.configure(text="Image Loaded. Press ANALYZE to start.", text_color="yellow")
            self.show_image_on_gui(filename)

    def minimize_app(self):
        self.iconify()

    def toggle_fullscreen(self):
        current_state = self.attributes('-fullscreen')
        self.attributes('-fullscreen', not current_state)

    def close_app(self):
        try:
            motor.finish_cycle()
        except:
            pass
        self.destroy()
        sys.exit()

    def reset_indicators(self):
        for i in range(1, NUM_CORNERS + 1):
            self.corner_widgets[i].configure(fg_color=COLOR_WAIT, text="WAITING")
        self.set_total_status("WAITING")

    # --- Update: Function accepting textual status ---
    def set_corner_status(self, corner_id, status_text):
        widget = self.corner_widgets.get(corner_id)
        if widget:
            if status_text == "CLASS A":
                widget.configure(fg_color=COLOR_PASS, text="PASS")
            elif status_text == "CLASS B":
                widget.configure(fg_color=COLOR_WARN, text="WARNING")
            elif status_text == "FAIL":
                widget.configure(fg_color=COLOR_FAIL, text="FAIL")
            else:
                widget.configure(fg_color=COLOR_WAIT, text="WAITING")

    def set_total_status(self, status):
        if status == "CLASS A":
            self.total_status_indicator.configure(fg_color=COLOR_PASS, text="CLASS A")
        elif status == "CLASS B":
            self.total_status_indicator.configure(fg_color=COLOR_WARN, text="CLASS B")
        elif status == "FAIL":
            self.total_status_indicator.configure(fg_color=COLOR_FAIL, text="FAIL")
        else:
            self.total_status_indicator.configure(fg_color=COLOR_WAIT, text="WAITING")

    def start_process_clicked(self):
        mode = self.mode_var.get()
        
        if mode == "Live Inspection":
            sn = self.entry_sn.get().strip()
            if not sn:
                self.status_label.configure(text="Error: Please enter SN first!", text_color="red")
                return
            
            self.btn_start.configure(state="disabled", text="RUNNING...")
            self.entry_sn.configure(state="disabled")
            self.mode_switch.configure(state="disabled") 
            self.reset_indicators()
            threading.Thread(target=self.run_live_logic, args=(sn,), daemon=True).start()

        else: # File Mode
            if not self.selected_file_path:
                self.status_label.configure(text="Error: Please choose a file first!", text_color="red")
                return
            
            self.btn_start.configure(state="disabled", text="PROCESSING...")
            threading.Thread(target=self.run_file_logic, args=(self.selected_file_path,), daemon=True).start()

    # --- File Analysis Logic ---
    def run_file_logic(self, file_path):
        try:
            self.update_progress(0.2)
            self.update_status("Analyzing Image...", "yellow")
            time.sleep(0.5) 

            # Expectation: Function returns string: "CLASS A", "CLASS B" or "FAIL"
            status_result = yellow_algo.check_yellow_defect(file_path)
            self.update_progress(0.8)

            dir_name = os.path.dirname(file_path)
            base_name = os.path.basename(file_path)
            name_no_ext = os.path.splitext(base_name)[0]
            result_path = os.path.join(dir_name, f"{name_no_ext}_YELLOW_RESULT.PNG")

            self.show_image_on_gui(result_path)
            self.update_progress(1.0)

            # Status Handling
            if status_result == "FAIL":
                self.update_status(f"Result: {status_result} ❌", "red")
                self.after(0, lambda: self.set_total_status("FAIL"))
                #buzzer.beep_fail()
            else:
                # Both CLASS A and CLASS B are passing
                icon = "✅" if status_result == "CLASS A" else "⚠️"
                color = "green" if status_result == "CLASS A" else "orange"
                
                self.update_status(f"Result: {status_result} {icon}", color)
                self.after(0, lambda: self.set_total_status(status_result)) 

        except Exception as e:
            print(f"Error: {e}")
            self.update_status("Analysis Error", "red")
        
        finally:
            self.after(0, lambda: self.btn_start.configure(state="normal", text="ANALYZE IMAGE"))

    # --- Live Inspection Logic ---
    def run_live_logic(self, serial_number):
        try:
            self.update_status("Initializing Motor & Camera...", "yellow")
            motor.reset_sequence()
            
            component_folder = os.path.join(RESULTS_BASE_FOLDER, f"SN_{serial_number}")
            if not os.path.exists(component_folder):
                os.makedirs(component_folder)

            # Variable to track the worst status found
            # Severity order: CLASS A (Best) -> CLASS B -> FAIL (Worst)
            final_component_status = "CLASS A"

            for i in range(NUM_CORNERS):
                corner_id = i + 1
                progress_val = i / NUM_CORNERS
                self.update_progress(progress_val)
                self.update_status(f"Inspecting Corner {corner_id}/4...", "white")
                
                filename = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}.PNG")
                
                if not cam.take_picture(filename):
                    self.update_status("Camera Error!", "red")
                    buzzer.beep_fail()
                    final_component_status = "FAIL"
                    break

                # Call algorithm - returns string
                status_result = yellow_algo.check_yellow_defect(filename)
                
                result_img_path = os.path.join(component_folder, f"corner_{corner_id}_{serial_number}_YELLOW_RESULT.PNG")
                self.show_image_on_gui(result_img_path)
                
                # Update specific corner indicator
                self.after(0, lambda c=corner_id, s=status_result: self.set_corner_status(c, s))

                if status_result == "FAIL":
                    self.update_status(f"Defect at Corner {corner_id}!", "red")
                    #buzzer.beep_fail()
                    final_component_status = "FAIL"
                    break # Stop on fail
                
                elif status_result == "CLASS B":
                    # Record minor defect, but continue inspection
                    if final_component_status == "CLASS A":
                        final_component_status = "CLASS B"

                # else: # CLASS A
                    # buzzer.beep_ok()

                if i < NUM_CORNERS - 1:
                    self.update_status(f"Rotating to next corner...", "cyan")
                    motor.rotate_to_next_corner()
            
            self.update_progress(1.0)
            self.update_status("Returning to Start Position...", "orange")
            time.sleep(0.5)
            motor.finish_cycle() 

            # Final Summary
            if final_component_status == "FAIL":
                self.update_status(f"SN: {serial_number} - FAILED ❌", "red")
            elif final_component_status == "CLASS B":
                self.update_status(f"SN: {serial_number} - CLASS B ⚠️", "orange")
            else:
                self.update_status(f"SN: {serial_number} - CLASS A ✅", "green")
                
            self.after(0, lambda: self.set_total_status(final_component_status))

        except Exception as e:
            print(f"CRITICAL ERROR: {e}")
            self.update_status("System Error!", "red")
        
        finally:
            self.after(0, lambda: self.btn_start.configure(state="normal", text="START INSPECTION"))
            self.after(0, lambda: self.entry_sn.configure(state="normal"))
            self.after(0, lambda: self.mode_switch.configure(state="normal"))

    def update_status(self, text, color="white"):
        self.after(0, lambda: self.status_label.configure(text=text, text_color=color))

    def update_progress(self, val):
        self.after(0, lambda: self.progress_bar.set(val))

    def show_image_on_gui(self, img_path):
        if os.path.exists(img_path):
            try:
                pil_img = Image.open(img_path)
                ctk_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(1000, 500))
                self.after(0, lambda: self.image_display.configure(image=ctk_img, text=""))
            except Exception as e:
                print(f"Error showing image: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
