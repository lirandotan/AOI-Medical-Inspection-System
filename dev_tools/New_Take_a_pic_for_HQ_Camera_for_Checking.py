from picamera2 import Picamera2
import cv2
import numpy as np

# Ask user for a file name (without extension)
image_name = input("Enter a name for the photo (without .PNG): ").strip() or "photo"
filename = f"{image_name}.PNG"

picam2 = Picamera2()

# 1) Fast preview configuration (good FPS for live view)
preview_config = picam2.create_preview_configuration(main={"size": (1280, 720)})
picam2.configure(preview_config)
picam2.start()

print("📷 Live view started.")
print("Press 's' to capture FULL-RES still (HQ).")
print("Press 'q' to quit without saving.")

# Pre-build a sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]], dtype=np.float32)

# Prepare a full-res still configuration for HQ (IMX477)
still_config = picam2.create_still_configuration(main={"size": (4056, 3040)})

while True:
    # Get latest RGB frame and convert to BGR for OpenCV display
    frame = cv2.cvtColor(picam2.capture_array(), cv2.COLOR_RGB2BGR)
    cv2.imshow("Live View (Preview)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # 2) Switch to full-res still, capture to array, then back to preview
        request = picam2.switch_mode_and_capture_array(still_config)
        fullres_bgr = cv2.cvtColor(request, cv2.COLOR_RGB2BGR)

        # Optional: sharpen before saving
        sharpened = cv2.filter2D(fullres_bgr, -1, kernel)

        # Save the sharpened full-res image
        cv2.imwrite(filename, sharpened)
        print(f"✅ Photo saved as {filename}")
        break

    elif key == ord('q'):
        print("❌ Quit without saving.")
        break

cv2.destroyAllWindows()
picam2.stop()
picam2.close()
