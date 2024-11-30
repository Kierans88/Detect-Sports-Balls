import os
import shutil

# Define paths
images_folder = "Football dataset/no_sports_ball/images"
labels_folder = "Football dataset/no_sports_ball/labels"
moved_files_folder = "Moved files"

# Create the destination folder if it doesn't exist
os.makedirs(moved_files_folder, exist_ok=True)

# Get a list of .txt files in the images folder
images_txt_files = {
    os.path.splitext(f)[0] for f in os.listdir(images_folder) if f.endswith(".txt")
}

# Check .txt files in the labels folder
for label_file in os.listdir(labels_folder):
    if label_file.endswith(".txt"):
        label_name = os.path.splitext(label_file)[0]
        # If a matching .txt exists in the images folder, move it to the new folder
        if label_name in images_txt_files:
            source_path = os.path.join(labels_folder, label_file)
            destination_path = os.path.join(moved_files_folder, label_file)
            shutil.move(source_path, destination_path)
            print(f"Moved: {source_path} to {destination_path}")

print("File relocation complete!")