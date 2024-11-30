import cv2
import os

# Input and output folder paths
input_folder = "Testing data/v1"  # Replace with the path to your folder containing input videos
output_folder = "Testing data/v2"  # Replace with the path to your desired output folder

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process all files in the input folder
for filename in os.listdir(input_folder):
    input_video_path = os.path.join(input_folder, filename)
    
    # Skip non-video files
    if not filename.lower().endswith('.mp4'):
        print(f"Skipping non-video file: {filename}")
        continue

    # Open the input video
    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        print(f"Error: Unable to open video file {filename}")
        continue

    # Get the original video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for output video
    width, height = 640, 480

    # Create the output video path
    output_video_path = os.path.join(output_folder, f"resized_{filename}")

    # Create VideoWriter object for the output video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Process each frame
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Exit loop when video ends
        
        # Resize the frame to 640x480
        resized_frame = cv2.resize(frame, (width, height))
        
        # Write the resized frame to the output file
        out.write(resized_frame)

    # Release resources
    cap.release()
    out.release()
    print(f"Processed and saved: {output_video_path}")

print("All videos processed!")
