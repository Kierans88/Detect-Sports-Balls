import os
import shutil

# Paths to the original 'output_annotations' folder
original_dir = 'output_annotations'

# Output directory where we'll organize the dataset
output_dataset_dir = 'dataset'

# Create directories for images and labels
images_dir = os.path.join(output_dataset_dir, 'images')
labels_dir = os.path.join(output_dataset_dir, 'labels')

# Create the directories if they don't exist
os.makedirs(images_dir, exist_ok=True)
os.makedirs(labels_dir, exist_ok=True)

# List all image files in the original directory
image_files = [f for f in os.listdir(original_dir) if f.endswith('.jpg')]

# Move images and their corresponding labels into the respective folders
for file in image_files:
    # Move the image file
    image_path = os.path.join(original_dir, file)
    shutil.copy(image_path, os.path.join(images_dir, file))

    # Move the corresponding label file
    label_file = file.replace('.jpg', '.txt')
    label_path = os.path.join(original_dir, label_file)
    
    # Check if the corresponding label file exists
    if os.path.exists(label_path):
        shutil.copy(label_path, os.path.join(labels_dir, label_file))
    else:
        print(f"Warning: Label file for {file} does not exist!")

print(f"Images and labels have been separated into their respective folders.")
