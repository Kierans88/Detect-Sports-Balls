import os

# Set paths to your images and labels folders
images_folder = 'Football dataset/no_sports_ball/images'
labels_folder = 'Football dataset/no_sports_ball/labels'

# Get list of filenames (without extension) from both folders
image_files = set(os.path.splitext(f)[0] for f in os.listdir(images_folder) if f.endswith('.txt'))
label_files = set(os.path.splitext(f)[0] for f in os.listdir(labels_folder) if f.endswith('.txt'))

# Iterate through label files and delete the ones that are also in the images folder
for label_file in label_files:
    if label_file in image_files:
        label_file_path = os.path.join(labels_folder, label_file + '.txt')
        os.remove(label_file_path)
        print(f"Deleted incorrect file: {label_file_path}")

print("Process complete.")
