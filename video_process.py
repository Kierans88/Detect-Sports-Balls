import os
import cv2
from ultralytics import YOLO

# Paths
video_path = "sports-1m-dataset/association_football/Futbol Skills Volume 3.mp4"
output_dir = "Football dataset"
sports_ball_images_dir = os.path.join(output_dir, "sports_ball/images")
sports_ball_labels_dir = os.path.join(output_dir, "sports_ball/labels")
no_sports_ball_images_dir = os.path.join(output_dir, "no_sports_ball/images")
no_sports_ball_labels_dir = os.path.join(output_dir, "no_sports_ball/labels")

# Create directories
os.makedirs(sports_ball_images_dir, exist_ok=True)
os.makedirs(sports_ball_labels_dir, exist_ok=True)
os.makedirs(no_sports_ball_images_dir, exist_ok=True)
os.makedirs(no_sports_ball_labels_dir, exist_ok=True)

# Load YOLO model
model = YOLO("yolov8m.pt")  # Replace with your model path if custom

# Define the sports ball class ID (check your YOLO model's classes.yaml file)
sports_ball_class_id = 32  # Adjust based on your model

# Open video file
cap = cv2.VideoCapture(video_path)
frame_count = 0

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Exit when video ends

    frame_count += 1
    
    # Stop at frame 1000
    if frame_count > 1000:
        break  # Exit if we reach frame 3000
    
    # Process only every 10th frame
    if frame_count % 10 != 0:
        continue  # Skip frames that are not multiples of 10
    
    print(f"Processing Frame {frame_count}...")

    # Run YOLO predictions on the frame
    results = model.predict(frame, verbose=False)

    # Check if sports ball is detected
    annotations = []
    for box in results[0].boxes:  # Results are per frame
        if int(box.cls[0]) == sports_ball_class_id:  # Check class ID
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Bounding box coordinates
            confidence = box.conf[0]  # Confidence score

            # Convert to YOLO format
            img_height, img_width = frame.shape[:2]
            x_center = (x1 + x2) / 2 / img_width
            y_center = (y1 + y2) / 2 / img_height
            width = (x2 - x1) / img_width
            height = (y2 - y1) / img_height

            annotations.append(f"{sports_ball_class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    # Resize the frame to 640x480
    frame_resized = cv2.resize(frame, (640, 480))

    # Categorize and save the frame and annotations
    frame_filename = f"frame_Futbol_Skills_Volume{frame_count:04d}.jpg"
    label_filename = f"frame_Futbol_Skills_Volume{frame_count:04d}.txt"

    if annotations:  # Sports ball detected
        cv2.imwrite(os.path.join(sports_ball_images_dir, frame_filename), frame_resized)
        label_path = os.path.join(sports_ball_labels_dir, label_filename)
        with open(label_path, "w") as f:
            f.write("\n".join(annotations))
    else:  # No sports ball detected
        cv2.imwrite(os.path.join(no_sports_ball_images_dir, frame_filename), frame_resized)
        label_path = os.path.join(no_sports_ball_labels_dir, label_filename)
        with open(label_path, "w") as f:
            pass  # Create an empty label file

cap.release()
print("Video processing complete. Dataset organized into sports_ball and no_sports_ball folders.")
