import cv2
import numpy as np

# Read image
im = cv2.imread('/home/pda-chipping/Tile - Classification/Class B or Fail - with crack/ROI_Output/32_0331_broken_2th_corner_2_ROI4.PNG')

# Convert BGR to HSV
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

# Define yellow range (experiment with values!)
h_low, h_high = 15, 35   # Hue range for yellow
s_low, s_high = 60, 199 # Saturation range
v_low, v_high = 90, 199 # Value range

# Create binary mask
bw = cv2.inRange(hsv, (h_low, s_low, v_low), (h_high, s_high, v_high))

# Morphological cleanup
kernel = np.ones((5,5), np.uint8)
opened = cv2.morphologyEx(bw, cv2.MORPH_OPEN, kernel)


# ---------- ספירת פיקסלים לבנים ----------
white_pixels = cv2.countNonZero(opened)
print("Number of white pixels in mask:", white_pixels)

# אם תרצה גם אחוזים מתוך כל התמונה:
total_pixels = opened.size
percent_white = (white_pixels / total_pixels) * 100
print("White area percentage:", percent_white, "%")

# Resize for display
display_width = 600
h_img, w_img = im.shape[:2]
scale = display_width / w_img
display_height = int(h_img * scale)

im_small = cv2.resize(im, (display_width, display_height), interpolation=cv2.INTER_AREA)
opened_small = cv2.resize(opened, (display_width, display_height), interpolation=cv2.INTER_NEAREST)

opened_color = cv2.cvtColor(opened_small, cv2.COLOR_GRAY2BGR)
combined = np.hstack((im_small, opened_color))

# ---------- פונקציה לבדיקת ערכים בלחיצה ----------
def pick_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # התאמה מהתמונה המוקטנת לגודל המקורי
        scale_x = w_img / display_width
        scale_y = h_img / display_height
        orig_x = int(x * scale_x)
        orig_y = int(y * scale_y)

        pixel = hsv[orig_y, orig_x]
        print(f"Pixel at ({orig_x},{orig_y}) -> H:{pixel[0]} S:{pixel[1]} V:{pixel[2]}")

# יצירת חלון והוספת callback
cv2.namedWindow("Original (left) + Mask (right)")
cv2.setMouseCallback("Original (left) + Mask (right)", pick_color)

cv2.imshow("Original (left) + Mask (right)", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()

