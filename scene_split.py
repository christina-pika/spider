import os
import subprocess

# Directory containing the MP4 files
video_dir = "/home/christina/data_youtube/BrunoSaraviaPhotography"

# List all files in the directory
files = os.listdir(video_dir)

# Filter out files that are not MP4
mp4_files = [file for file in files if file.endswith('.mp4')]

# Loop through each MP4 file and run the scenedetect command
for mp4_file in mp4_files:
    # Construct the full path to the MP4 file
    full_path = os.path.join(video_dir, mp4_file)
    
    # Construct the scenedetect command
    command = f"scenedetect -i \"{full_path}\" split-video"
    
    # Execute the command
    subprocess.run(command, shell=True)
