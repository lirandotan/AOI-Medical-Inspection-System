import time
import cv2
import numpy as np
from picamera2 import Picamera2

def take_picture(filename):
    """
    מאתחל מצלמה, מצלם תמונה אחת באיכות גבוהה, ומבצע חידוד.
    """
    print(f"📷 [Camera] Capturing {filename}...")
    
    try:
        picam2 = Picamera2()
        # תצורת Still HQ
        config = picam2.create_still_configuration(main={"size": (4056, 3040)})
        picam2.configure(config)
        picam2.start()
        
        # זמן להתייצבות (חובה לפוקוס ואיזון לבן)
        time.sleep(2) 
        
        # צילום
        image_data = picam2.capture_array()
        picam2.stop()
        picam2.close()
        
        # עיבוד תמונה
        image_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
        
        # קרנל לחידוד
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]], dtype=np.float32)
        sharpened = cv2.filter2D(image_bgr, -1, kernel)
        
        # שמירה
        cv2.imwrite(filename, sharpened)
        return True
        
    except Exception as e:
        print(f"❌ [Camera Error] {e}")
        return False
