import os

# Define the folder containing your annotations
annotation_folder = 'Football dataset/sports_ball/labels'  

# Loop through all files in the folder
for filename in os.listdir(annotation_folder):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        file_path = os.path.join(annotation_folder, filename)
        
        # Open the file and read its content
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # If the file is not empty, process it
        if lines:
            modified_lines = []
            for line in lines:
                # Split the line into its components
                parts = line.strip().split()
                
                # Check if the class ID is 32 and change it to 1
                if parts[0] == '32':
                    parts[0] = '1'
                
                # Join the parts back into a line and add to the modified list
                modified_lines.append(' '.join(parts))
            
            # Write the modified content back to the file
            with open(file_path, 'w') as file:
                file.write('\n'.join(modified_lines) + '\n')
        else:
            print(f"File {filename} is empty, skipping...")
    else:
        print(f"Skipping non-annotation file: {filename}")

print("Processing complete.")
