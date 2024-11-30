import os
import shutil

# Define source folder and target folders
source_folder = "Football dataset/no_sports_ball/images"  # Replace with your source folder path if different
image_target_folder = "Football dataset/sports_ball/images"
label_target_folder = "Football dataset/sports_ball/labels"

# Create target folders if they don't exist
os.makedirs(image_target_folder, exist_ok=True)
os.makedirs(label_target_folder, exist_ok=True)

# Iterate through the files in the source folder
for file in os.listdir(source_folder):
    # Check if the file is a .jpg
    if file.endswith(".jpg"):
        base_name = os.path.splitext(file)[0]  # Get the filename without extension
        txt_file = f"{base_name}.txt"
        
        # Check if the corresponding .txt exists
        if txt_file in os.listdir(source_folder):
            # Move the .jpg to the image target folder
            shutil.move(os.path.join(source_folder, file), os.path.join(image_target_folder, file))
            # Move the .txt to the label target folder
            shutil.move(os.path.join(source_folder, txt_file), os.path.join(label_target_folder, txt_file))

print("Files have been moved successfully!")
