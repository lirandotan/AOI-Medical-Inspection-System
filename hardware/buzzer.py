#########--------ONLY PASS/FAIL ---------------------------------------#################

# import time
# from gpiozero import OutputDevice

# BUZZER_PIN = 25
# _buzzer_device = None

# def init():
    # global _buzzer_device
    # if _buzzer_device is None:
        # _buzzer_device = OutputDevice(BUZZER_PIN, active_high=True, initial_value=False)

# def beep_warning():
   
    # init()
    # print("🔊 [Buzzer] OK Signal")
    # for _ in range(1):
        # _buzzer_device.on()
        # time.sleep(0.1)
        # _buzzer_device.off()
        # time.sleep(0.05)

# def beep_fail():
   
    # init()
    # print("🔊 [Buzzer] FAIL Signal")
    # for _ in range(2):
        # _buzzer_device.on()
        # time.sleep(0.1)
        # _buzzer_device.off()
        # time.sleep(0.2)

# def close():
    # global _buzzer_device
    # if _buzzer_device:
        # _buzzer_device.close()
        # _buzzer_device = None


##########------------- WITH CLASS B ----------------------------------------#####################


import time
from gpiozero import OutputDevice

BUZZER_PIN = 25
_buzzer_device = None

def init():
    global _buzzer_device
    if _buzzer_device is None:
        _buzzer_device = OutputDevice(BUZZER_PIN, active_high=True, initial_value=False)

def close():
    global _buzzer_device
    if _buzzer_device:
        _buzzer_device.close()
        _buzzer_device = None

# --- פונקציות הצפצוף ---

def beep_warning():
    """ צפצוף אחד קצר עבור CLASS B """
    init()
    print("🔊 [Buzzer] WARNING (Class B)")
    _buzzer_device.on()
    time.sleep(0.15)
    _buzzer_device.off()
    time.sleep(0.1)

def beep_fail():
    """ שני צפצופים קצרים עבור FAIL """
    init()
    print("🔊 [Buzzer] FAIL")
    for _ in range(2):
        _buzzer_device.on()
        time.sleep(0.1)
        _buzzer_device.off()
        time.sleep(0.1)
