import os
import cv2

def main():
    # Ask user for image path (can be full path or relative)
    image_path = input("Enter image filename or full path: ").strip().strip('"').strip("'")

    if not os.path.isfile(image_path):
        print("❌ Image not found.")
        return

    img = cv2.imread(image_path)
    if img is None:
        print("❌ Failed to read image.")
        return

    # Get image size
    H, W = img.shape[:2]

    # Compute central ROI size: one third of the width and height
    roi_w = max(1, W // 5)
    roi_h = max(1, H // 5)

    # Compute top-left corner so that ROI is centered
    x_start = (W - roi_w) // 2
    y_start = (H - roi_h) // 2
    x_end = x_start + roi_w
    y_end = y_start + roi_h

    # Safety clamp (should not be needed, but just in case)
    x_start = max(0, min(x_start, W - 1))
    y_start = max(0, min(y_start, H - 1))
    x_end   = max(0, min(x_end,   W))
    y_end   = max(0, min(y_end,   H))

    if x_end <= x_start or y_end <= y_start:
        print("⚠️ Invalid ROI, nothing to save.")
        return

    # Crop the central ROI
    roi = img[y_start:y_end, x_start:x_end]

    # Build output filename with 'ROI' suffix
    root, ext = os.path.splitext(image_path)
    if not ext:
        ext = ".PNG"  # default extension if none

    output_path = f"{root}_ROI4{ext}"

    ok = cv2.imwrite(output_path, roi)
    if ok:
        print(f"✅ Saved ROI: {output_path}")
        print(f"   x={x_start}, y={y_start}, w={roi_w}, h={roi_h}")
    else:
        print("❌ Failed to save ROI.")

if __name__ == "__main__":
    main()
    
    
    
####-------------------------FOR FOLDER--------------------------------------###
    
# import os
# import cv2

# def process_single_image(image_path, output_folder):
    # """
    # מעבד תמונה בודדת: חותך את המרכז ושומר בתיקיית היעד
    # """
    # img = cv2.imread(image_path)
    # if img is None:
        # # מדלג אם הקובץ פגום או לא תמונה
        # return

    # H, W = img.shape[:2]

    # # חישוב גודל החיתוך (רבע מהרוחב והגובה)
    # roi_w = max(1, W // 4)
    # roi_h = max(1, H // 4)

    # # חישוב נקודת ההתחלה כדי שהחיתוך יהיה במרכז
    # x_start = (W - roi_w) // 2
    # y_start = (H - roi_h) // 2
    # x_end = x_start + roi_w
    # y_end = y_start + roi_h

    # # בדיקות תקינות (Safety clamp)
    # x_start = max(0, min(x_start, W - 1))
    # y_start = max(0, min(y_start, H - 1))
    # x_end   = max(0, min(x_end,   W))
    # y_end   = max(0, min(y_end,   H))

    # # ביצוע החיתוך
    # roi = img[y_start:y_end, x_start:x_end]

    # # יצירת שם קובץ חדש
    # filename = os.path.basename(image_path)
    # root, ext = os.path.splitext(filename)
    # if not ext:
        # ext = ".PNG"
    
    # output_filename = f"{root}_ROI4{ext}"
    # output_path = os.path.join(output_folder, output_filename)

    # # שמירה
    # ok = cv2.imwrite(output_path, roi)
    # if ok:
        # print(f"✅ Saved: {output_filename}")
    # else:
        # print(f"❌ Failed to save: {output_filename}")

# def main():
    # # --- שלב 1: בקשת הנתיב מהמשתמש ---
    # print("\n" + "="*40)
    # # הפקודה הזו עוצרת את התוכנה ומחכה שתדביק נתיב ותלחץ אנטר
    # folder_path = input("📂 Please paste the folder path here: ").strip().strip('"').strip("'")
    # print("="*40 + "\n")

    # # בדיקה שהתיקייה קיימת
    # if not os.path.isdir(folder_path):
        # print("❌ Error: The folder path does not exist.")
        # return

    # # --- שלב 2: יצירת תיקיית פלט ---
    # output_dir = os.path.join(folder_path, "ROI_Output")
    # if not os.path.exists(output_dir):
        # os.makedirs(output_dir)
        # print(f"Created output folder: {output_dir}\n")
    # else:
        # print(f"Output folder exists: {output_dir}\n")

    # # --- שלב 3: ריצה על כל הקבצים ---
    # valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp')
    # count = 0

    # files = os.listdir(folder_path)
    # print(f"Found {len(files)} files in directory. Processing images...\n")

    # for filename in files:
        # if filename.lower().endswith(valid_extensions):
            # full_path = os.path.join(folder_path, filename)
            # process_single_image(full_path, output_dir)
            # count += 1

    # print("\n" + "-"*30)
    # print(f"🎉 Done! Processed {count} images.")
    # print(f"📁 Results are in: {output_dir}")
    # print("-"*30)

# if __name__ == "__main__":
    # main()
