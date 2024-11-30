# ID for 'football' label
target_video_id = '368'

# Open the file with video links and IDs
with open('sports-1m-dataset/original/test_partition.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Filter the lines to find the video associated with the ID 357
video_links_with_indices = []  # List to store tuples of (index, URL)

for index, line in enumerate(lines):
    line = line.strip()  # Strip leading/trailing spaces
    
    # Skip empty lines or incorrectly formatted lines
    if not line:
        continue
    
    # Split the line into video URL and ID
    try:
        url, video_ids = line.split()  # Split into URL and IDs
    except ValueError:
        print(f"Skipping incorrectly formatted line: {line}")
        continue  # Skip lines that don't have exactly two parts (URL and video IDs)
    
    # Check if the target video ID is in the list of IDs
    if target_video_id in video_ids.split(','):
        video_links_with_indices.append((index, url))  # Store index and URL

# Print the indices and video URLs linked to ID 357
for idx, link in video_links_with_indices:
    print(f"Index: {idx}, URL: {link}")
