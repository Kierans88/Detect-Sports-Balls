import os
import shutil
import random

# Set your paths
image_dir = "full images"  # Path to your images folder
label_dir = "full labels"  # Path to your labels folder
dataset_dir = "dataset"  # Path for the new dataset folder
train_image_dir = os.path.join(dataset_dir, "train/images")
val_image_dir = os.path.join(dataset_dir, "val/images")
train_label_dir = os.path.join(dataset_dir, "train/labels")
val_label_dir = os.path.join(dataset_dir, "val/labels")

# Create dataset, train, and val directories if they don't exist
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(val_image_dir, exist_ok=True)
os.makedirs(train_label_dir, exist_ok=True)
os.makedirs(val_label_dir, exist_ok=True)

# Get the list of image files (only .jpg files)
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

# Shuffle the image files randomly
random.seed(1)  # Optional, for reproducibility
random.shuffle(image_files)

# Calculate the number of images for training (70%)
train_size = int(len(image_files) * 0.7)

# Split the files into training and testing (validation)
train_images = image_files[:train_size]
val_images = image_files[train_size:]

# Move the images and labels to the corresponding directories
for image in train_images:
    # Move image
    shutil.move(os.path.join(image_dir, image), os.path.join(train_image_dir, image))
    # Move corresponding label file
    label_file = image.replace('.jpg', '.txt')
    shutil.move(os.path.join(label_dir, label_file), os.path.join(train_label_dir, label_file))

for image in val_images:
    # Move image
    shutil.move(os.path.join(image_dir, image), os.path.join(val_image_dir, image))
    # Move corresponding label file
    label_file = image.replace('.jpg', '.txt')
    shutil.move(os.path.join(label_dir, label_file), os.path.join(val_label_dir, label_file))

print(f"Training set: {len(train_images)} images")
print(f"Validation set: {len(val_images)} images")
