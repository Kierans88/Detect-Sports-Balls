import os
import yt_dlp as ytdlp

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

# Mapping of sports to their corresponding indices
sports_videos = {
    "association_football": association_football_indices,
}

# Parent directory for storing videos
parent_dir = "sports-1m-dataset"

# Ensure sport-specific folders exist
os.makedirs(parent_dir, exist_ok=True)
for sport in sports_videos.keys():
    os.makedirs(os.path.join(parent_dir, sport), exist_ok=True)

# Function to download videos using yt-dlp
def download_video(url, sport):
    try:
        # Generate the output path based on the URL and sport
        output_path = os.path.join(parent_dir, sport, '%(title)s.%(ext)s')
        
        # Check if the file already exists
        if os.path.exists(output_path):
            print(f"Video already downloaded: {url}")
            return  # Skip download if the file exists
        
        print(f"Downloading {url} for {sport}...")
        ydl_opts = {
            'outtmpl': output_path,  # Output path for video
            'format': 'bestvideo',  # Only best video quality (no audio)
        }
        with ytdlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        print(f"Downloaded: {url}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Download videos for each sport using the stored URLs
for sport, indices in sports_videos.items():
    for idx in indices:
        if idx in index_to_url:
            url = index_to_url[idx]
            download_video(url, sport)

print("All downloads complete.")
