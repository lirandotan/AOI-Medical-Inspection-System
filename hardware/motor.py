# import time
# from gpiozero import DigitalOutputDevice

# # הגדרות פינים
# PULSE_PIN = 18
# DIR_PIN = 24

# def move_steps(steps, direction="CW", min_delay=0.005, start_delay=0.02):
    # """
    # מזיז את המנוע עם האצה והאטה (Ramping) למניעת החלקות.
    
    # :param steps: מספר הצעדים לביצוע
    # :param direction: כיוון ("CW" או "CCW")
    # :param min_delay: המהירות המקסימלית (המספר הכי נמוך = הכי מהיר). ברירת מחדל 0.005
    # :param start_delay: מהירות ההתחלה האיטית. ברירת מחדל 0.02
    # """
    # pulse = DigitalOutputDevice(PULSE_PIN)
    # dir_pin = DigitalOutputDevice(DIR_PIN)
    
    # try:
        # # קביעת כיוון
        # if direction == "CW":
            # dir_pin.on()
        # else:
            # dir_pin.off()
        
        # print(f"⚙️ [Motor] Moving {steps} steps ({direction}) with Ramping...")
        
        # # חישוב אורך הרמפה (כמה צעדים יוקדשו להאצה וכמה להאטה)
        # # נקדיש 20% מהדרך להאצה ו-20% להאטה, אלא אם מספר הצעדים קטן מאוד
        # ramp_steps = int(steps * 0.2)
        # if ramp_steps < 2: ramp_steps = 0 # ביטול האצה בתנועות זעירות
        
        # current_delay = start_delay

        # for i in range(steps):
            # # --- חישוב העיכוב (Delay) לצעד הנוכחי ---
            
            # # שלב 1: האצה (בתחילת התנועה)
            # if i < ramp_steps:
                # # אנחנו מקטינים את הדיליי ליניארית מ-start_delay ל-min_delay
                # progress = i / ramp_steps
                # current_delay = start_delay - (progress * (start_delay - min_delay))
            
            # # שלב 2: האטה (בסוף התנועה)
            # elif i >= steps - ramp_steps:
                # # אנחנו מגדילים את הדיליי בחזרה
                # steps_left = steps - i
                # progress = (ramp_steps - steps_left) / ramp_steps
                # # משתמשים באותה נוסחה הפוכה
                # current_delay = min_delay + (progress * (start_delay - min_delay))
            
            # # שלב 3: שיוט (אמצע התנועה)
            # else:
                # current_delay = min_delay

            # # --- ביצוע הצעד ---
            # pulse.on()
            # time.sleep(current_delay)
            # pulse.off()
            # time.sleep(current_delay)
            
    # except Exception as e:
        # print(f"❌ [Motor Error] {e}")
    # finally:
        # pulse.close()
        # dir_pin.close()


########-----------------------------------------------------------##########


# import time
# from gpiozero import DigitalOutputDevice

# # הגדרות פינים
# PULSE_PIN = 18
# DIR_PIN = 24

# def move_steps(steps, direction="CW", speed_delay=0.02): #speed_delay=0.005
    # """
    # מזיז את המנוע מספר צעדים.
    # """
    # pulse = DigitalOutputDevice(PULSE_PIN)
    # dir_pin = DigitalOutputDevice(DIR_PIN)
    
    # try:
        # if direction == "CW":
            # dir_pin.on()
        # else:
            # dir_pin.off()
        
        # print(f"⚙️ [Motor] Moving {steps} steps ({direction})...")
        
        # for _ in range(steps):
            # pulse.on()
            # time.sleep(speed_delay)
            # pulse.off()
            # time.sleep(speed_delay)
            
    # except Exception as e:
        # print(f"❌ [Motor Error] {e}")
    # finally:
        # # סגירה בטוחה של הפינים
        # pulse.close()
        # dir_pin.close()



# #####----------------- WITH THE RELAY !!! GOOD.... BUT NOT PERFECT------------------------------------------###########


# import time
# from gpiozero import DigitalOutputDevice

# # --- הגדרות פינים ---
# PULSE_PIN = 18
# DIR_PIN = 24
# RELAY_PIN = 23  # הפין שאליו חיברת את ה-IN של הממסר (שנה אם חיברת לאחר)

# def move_steps(steps, direction="CW", speed_delay=0.02):
    # """
    # מזיז את המנוע:
    # 1. מדליק ממסר (נותן כוח לדרייבר)
    # 2. מבצע צעדים
    # 3. מכבה ממסר (מנתק כוח)
    # """
    # # יצירת אובייקטים לפינים
    # pulse = DigitalOutputDevice(PULSE_PIN)
    # dir_pin = DigitalOutputDevice(DIR_PIN)
    # motor_relay = DigitalOutputDevice(RELAY_PIN)
    
    # try:
        # # --- שלב 1: הדלקת מתח למנוע ---
        # # print("⚡ Powering Motor ON...") # (אופציונלי להדפסה)
        # motor_relay.on()  # סגירת הממסר - זרם זורם לדרייבר
        # time.sleep(0.2)   # המתנה קצרה שהממסר יתייצב והקבלים בדרייבר ייטענו
        
        # # --- שלב 2: הגדרת כיוון ---
        # if direction == "CW":
            # dir_pin.on()
        # else:
            # dir_pin.off()
        
        # print(f"⚙️ [Motor] Moving {steps} steps ({direction})...")
        
        # # --- שלב 3: ביצוע הצעדים ---
        # for _ in range(steps):
            # pulse.on()
            # time.sleep(speed_delay)
            # pulse.off()
            # time.sleep(speed_delay)
            
    # except Exception as e:
        # print(f"❌ [Motor Error] {e}")

    # finally:
        # # --- שלב 4: כיבוי וניתוק ---
        # # print("💤 Powering Motor OFF...") # (אופציונלי להדפסה)
        # motor_relay.off()  # כיבוי הממסר - המנוע מתנתק ממתח
        
        # # סגירה בטוחה של הפינים (שחרור משאבים)
        # pulse.close()
        # dir_pin.close()
        # motor_relay.close()


######---------------TRY CLOSE THE MOTOR - FAILED !!!------##############################################


# import time
# from gpiozero import DigitalOutputDevice

# --- הגדרות פינים ---
# PULSE_PIN = 18
# DIR_PIN = 24
# RELAY_PIN = 23

# --- יצירת האובייקטים באופן גלובלי (פעם אחת) ---
# כך הם נשארים זמינים תמיד לכיבוי חירום
# pulse = DigitalOutputDevice(PULSE_PIN)
# dir_pin = DigitalOutputDevice(DIR_PIN)
# motor_relay = DigitalOutputDevice(RELAY_PIN)

# def turn_off():
    # """
    # פונקציית חירום לכיבוי הממסר והמנוע.
    # נקרא לה מהקובץ הראשי כשהתוכנה נסגרת.
    # """
    # try:
        # motor_relay.off()
        # pulse.off() # אופציונלי
        # print("🛑 Motor Relay Forced OFF.")
    # except:
        # pass

# def close_resources():
    # """סגירה מסודרת של הפינים"""
    # pulse.close()
    # dir_pin.close()
    # motor_relay.close()

# def move_steps(steps, direction="CW", speed_delay=0.02):
    # """
    # מזיז את המנוע עם הגנה של הממסר.
    # """
    # try:
        # 1. הדלקת ממסר
        # motor_relay.on()
        # time.sleep(0.1) # זמן התייצבות
        
        # 2. כיוון
        # if direction == "CW":
            # dir_pin.on()
        # else:
            # dir_pin.off()
        
        # print(f"⚙️ [Motor] Moving {steps} steps ({direction})...")
        
        # 3. תנועה
        # for _ in range(steps):
            # pulse.on()
            # time.sleep(speed_delay)
            # pulse.off()
            # time.sleep(speed_delay)
            
    # except Exception as e:
        # print(f"❌ [Motor Error] {e}")

    # finally:
        # 4. כיבוי ממסר בסיום התנועה
        # motor_relay.off()


##----------------------DIFFRENT STEP PER CORNER - FOR CHECK----------------------------------####
# import time
# from gpiozero import DigitalOutputDevice

# # --- הגדרות פינים ---
# PULSE_PIN = 18
# DIR_PIN = 24
# RELAY_PIN = 23

# # --- הגדרות כיול אקסצנטריות (סה"כ 200 צעדים) ---
# # הרצף: פינה 1->2, 2->3, 3->4, 4->1
# STEPS_CYCLE = [45, 54, 42, 59]  #[46, 54, 42, 58] 

# # משתנה גלובלי פנימי ששומר איזה צלע אנחנו עכשיו (0 עד 3)
# _current_side_index = 0

# def reset_sequence():
    # """
    # מאפס את הספירה להתחלה.
    # חובה לקרוא לפונקציה הזו בתחילת בדיקה של רכיב חדש!
    # """
    # global _current_side_index
    # _current_side_index = 0
    # print("🔄 Motor sequence reset to Start (Side 1).")

# def move_raw_steps(steps, direction="CW", speed_delay=0.02):
    # """
    # הפונקציה המקורית שלך (Low Level) - מבצעת את הצעדים פיזית.
    # שיניתי את השם ל-raw כדי להבדיל אותה מהלוגיקה החדשה.
    # """
    # pulse = DigitalOutputDevice(PULSE_PIN)
    # dir_pin = DigitalOutputDevice(DIR_PIN)
    # motor_relay = DigitalOutputDevice(RELAY_PIN)
    
    # try:
        # motor_relay.on()
        # time.sleep(0.2)
        
        # if direction == "CW":
            # dir_pin.on()
        # else:
            # dir_pin.off()
        
        # # print(f"⚙️ Moving {steps} steps...") # אפשר להחזיר אם רוצים
        
        # for _ in range(steps):
            # pulse.on()
            # time.sleep(speed_delay)
            # pulse.off()
            # time.sleep(speed_delay)
            
    # except Exception as e:
        # print(f"❌ [Motor Error] {e}")

    # finally:
        # motor_relay.off()
        # pulse.close()
        # dir_pin.close()
        # motor_relay.close()

# def rotate_to_next_corner():
    # """
    # הפונקציה החדשה שה-Main צריך לקרוא לה.
    # היא מחשבת לבד כמה צעדים צריך לפי התור.
    # """
    # global _current_side_index
    
    # # 1. בדיקה כמה צעדים צריך עכשיו
    # steps_needed = STEPS_CYCLE[_current_side_index]
    
    # print(f"⚙️ [Motor] Rotating to next corner: {steps_needed} steps (Index: {_current_side_index})")
    
    # # 2. ביצוע התנועה
    # move_raw_steps(steps_needed)
    
    # # 3. קידום האינדקס לפעם הבאה (בצורה מעגלית 0-3)
    # _current_side_index = (_current_side_index + 1) % 4
    
    
##--------------DIFFRENT STEP PER CORNER - RETURN TO START POINT - LOWER SPEED -------------###
    
import time
from gpiozero import DigitalOutputDevice

# --- הגדרות פינים ---
PULSE_PIN = 18
DIR_PIN = 24
RELAY_PIN = 23

# --- הגדרות כיול (סה"כ 200 צעדים) ---
# הרצף: פינה 1->2, 2->3, 3->4, 4->1
STEPS_CYCLE =  [46, 59, 41, 55] #[46, 54, 42, 58] #[46, 59, 43, 55] #[46, 59, 41, 55]

# משתנה פנימי ששומר איזה צלע אנחנו עכשיו (0 עד 3)
_current_side_index = 0

def reset_sequence():
    """ 
    מאפס את הספירה להתחלה.
    חובה לקרוא לפונקציה הזו בתחילת בדיקה של רכיב חדש!
    """
    global _current_side_index
    _current_side_index = 0
    print(" Motor sequence reset to Start (Side 1).")

def move_raw_steps(steps, direction="CW", speed_delay=0.1): #speed_delay=0.07
    """
    הפונקציה המקורית (Low Level) - מבצעת את הצעדים פיזית.
    המהירות (speed_delay) הוגדרה ל-0.05 לתנועה איטית וחלקה יותר.
    """
    pulse = DigitalOutputDevice(PULSE_PIN)
    dir_pin = DigitalOutputDevice(DIR_PIN)
    motor_relay = DigitalOutputDevice(RELAY_PIN)
    
    try:
        motor_relay.on()
        time.sleep(0.2) # זמן קצר להתייצבות
        
        if direction == "CW":
            dir_pin.on()
        else:
            dir_pin.off()
        
        # print(f"⚙️ Moving {steps} steps...") 
        
        for _ in range(steps):
            pulse.on()
            time.sleep(speed_delay) # ההשהיה קובעת את המהירות
            pulse.off()
            time.sleep(speed_delay)
            
    except Exception as e:
        print(f"❌ [Motor Error] {e}")

    finally:
        motor_relay.off()
        pulse.close()
        dir_pin.close()
        motor_relay.close()

def rotate_to_next_corner():
    """
    הפונקציה שה-Main קורא לה.
    היא מחשבת לבד כמה צעדים צריך לפי התור.
    """
    global _current_side_index
    
    # 1. בדיקה כמה צעדים צריך עכשיו
    steps_needed = STEPS_CYCLE[_current_side_index]
    
    print(f"⚙️ [Motor] Rotating to next position ({steps_needed} steps)...")
    
    # 2. ביצוע התנועה
    move_raw_steps(steps_needed)
    
    # 3. קידום האינדקס לפעם הבאה (בצורה מעגלית 0-3)
    _current_side_index = (_current_side_index + 1) % 4

def finish_cycle():
    """
    פונקציה שמשלימה את הסיבוב עד לנקודת ההתחלה.
    קוראים לה בסוף הבדיקה (גם אם נכשלה) כדי להחזיר את המנוע ל-0.
    """
    global _current_side_index
    
    # אם אנחנו כבר ב-0, אין מה לעשות
    if _current_side_index == 0:
        return

    print("↩️ Returning to Start Position...")
    
    # כל עוד לא חזרנו ל-0, תמשיך לסובב
    while _current_side_index != 0:
        rotate_to_next_corner()
        time.sleep(1) # הפסקה קטנה בין תזוזות
        
    print(" Motor is back at Home Position.")
