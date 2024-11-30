import shutil
import os

# Define the source and destination paths
base_folder = 'Football dataset'
source_folders = ['no_sports_ball', 'sports_ball']
destination_images = 'images'
destination_labels = 'labels'

# Ensure destination directories exist
os.makedirs(destination_images, exist_ok=True)
os.makedirs(destination_labels, exist_ok=True)

# Loop over the source folders to copy images and labels
for folder in source_folders:
    images_folder = os.path.join(base_folder, folder, 'images')
    labels_folder = os.path.join(base_folder, folder, 'labels')
    
    # Copy images
    for image_file in os.listdir(images_folder):
        if image_file.endswith(('.jpg', '.png', '.jpeg')):  # Adjust the image extensions if needed
            shutil.copy(os.path.join(images_folder, image_file), destination_images)
    
    # Copy labels
    for label_file in os.listdir(labels_folder):
        if label_file.endswith('.txt'):  # Adjust the label extensions if needed
            shutil.copy(os.path.join(labels_folder, label_file), destination_labels)

print("Files copied successfully.")
