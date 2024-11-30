import os
import cv2

# Input and output directories
input_folder = "Football dataset/no_sports_ball/images"
output_folder = "annotated_images"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):  # Process only image files
        # Corresponding annotation file
        txt_file = os.path.splitext(filename)[0] + ".txt"
        txt_path = os.path.join(input_folder, txt_file)
        img_path = os.path.join(input_folder, filename)

        # Read the image
        image = cv2.imread(img_path)
        if image is None:
            print(f"Could not read image: {img_path}")
            continue

        height, width, _ = image.shape

        # Check if annotation file exists
        if os.path.exists(txt_path):
            with open(txt_path, "r") as file:
                for line in file:
                    # Parse the YOLO annotation
                    parts = line.strip().split()
                    if len(parts) != 5:
                        continue

                    class_id, x_center, y_center, box_width, box_height = map(float, parts)

                    # Convert YOLO normalized coordinates to pixel coordinates
                    x_center *= width
                    y_center *= height
                    box_width *= width
                    box_height *= height

                    x1 = int(x_center - box_width / 2)
                    y1 = int(y_center - box_height / 2)
                    x2 = int(x_center + box_width / 2)
                    y2 = int(y_center + box_height / 2)

                    # Draw the bounding box
                    color = (0, 255, 0)  # Green color for the bounding box
                    thickness = 2
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)

                    # Optional: Add class ID as label
                    label = f"Class {int(class_id)}"
                    cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, thickness)

        # Save the annotated image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, image)
        print(f"Saved annotated image: {output_path}")
