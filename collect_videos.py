# Indices of interest for each sport
association_football_indices = [211619, 188499, 102619, 50941, 2033]

# Combine all indices into one list
all_indices = (
    association_football_indices 
)

# Open the file with video links and IDs
with open('sports-1m-dataset/original/test_partition.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Create a dictionary to store URLs by index
index_to_url = {}

# Find the URLs corresponding to the indices
for idx in all_indices:
    # Ensure the index is within bounds
    if idx < len(lines):
        line = lines[idx].strip()  # Get the line at the given index
        url = line.split()[0]  # Extract the URL (first part of the line)
        index_to_url[idx] = url

# Print the results
for idx, url in index_to_url.items():
    print(f"Index: {idx}, URL: {url}")
