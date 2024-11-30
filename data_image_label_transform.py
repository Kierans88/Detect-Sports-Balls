import os
import cv2
import albumentations as A
import numpy as np

# Define paths
images_folder = "images"
labels_folder = "labels"
aug_images_folder = "aug_images"
aug_labels_folder = "aug_labels"

# Create output directories if they don't exist
os.makedirs(aug_images_folder, exist_ok=True)
os.makedirs(aug_labels_folder, exist_ok=True)

# Albumentations transformation (flip horizontally)
transform = A.Compose([
    A.HorizontalFlip(p=1.0),  # Always apply horizontal flip with probability 1
])

def flip_image_and_labels(image_path, label_path, aug_image_path, aug_label_path):
    # Load image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

    # Apply the flip transformation
    augmented = transform(image=image)
    flipped_image = augmented['image']

    # Save the flipped image
    flipped_image_bgr = cv2.cvtColor(flipped_image, cv2.COLOR_RGB2BGR)  # Convert back to BGR for saving
    cv2.imwrite(aug_image_path, flipped_image_bgr)
    
    # Check if label file exists
    if os.path.exists(label_path) and os.path.getsize(label_path) > 0:
        with open(label_path, 'r') as f:
            lines = f.readlines()

        # Open new label file to write flipped coordinates
        with open(aug_label_path, 'w') as f:
            for line in lines:
                parts = line.strip().split()
                class_id = parts[0]  # Class ID
                x_center, y_center, width, height = map(float, parts[1:])
                
                # Get image width (to flip horizontally)
                img_width = image.shape[1]
                
                # Flip the x_center coordinate
                x_center_flipped = 1 - x_center  # Flip horizontally
                
                # Write the new flipped label
                f.write(f"{class_id} {x_center_flipped} {y_center} {width} {height}\n")
    else:
        # If label is empty, keep it empty
        open(aug_label_path, 'w').close()

# Loop through images and their corresponding label files
for img_file in os.listdir(images_folder):
    if img_file.endswith('.jpg'):
        # Get image and label file paths
        image_path = os.path.join(images_folder, img_file)
        label_path = os.path.join(labels_folder, img_file.replace(img_file.split('.')[-1], 'txt'))
        
        # Create new filenames (e.g., "image_1.jpg" → "image_1_aug.jpg")
        base_name = os.path.splitext(img_file)[0]  # Get the base name without extension
        aug_image_name = base_name + '_aug' + os.path.splitext(img_file)[1]  # Append '_aug' to the filename
        aug_label_name = base_name + '_aug' + '.txt'  # Append '_aug' to the label filename
        
        # Define paths for augmented image and label
        aug_image_path = os.path.join(aug_images_folder, aug_image_name)
        aug_label_path = os.path.join(aug_labels_folder, aug_label_name)
        
        # Perform the flip and save
        flip_image_and_labels(image_path, label_path, aug_image_path, aug_label_path)

print("Data augmentation complete!")
