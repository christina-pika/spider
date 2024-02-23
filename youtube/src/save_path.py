import json
import os

set_file_path = os.path.join(os.path.dirname(__file__), '..', 'set.json')
with open(set_file_path, 'r') as set_file:
    settings = json.load(set_file)

json_file_path = settings["json_file_path"]
video_path = settings["settings"]

def save_video_paths():
    with open(json_file_path, 'r') as file:
        data = json.load(file)
        for video in data:
            title = video["original title (Title of the video)"]
            youtube_link = video["Youtube / Adobe Stock Link"]
            code = youtube_link.split('=')[-1]
            file_exists = False
            # Search for the file in video_download directory
            for filename in os.listdir(video_path):
                if filename.endswith(f"[{code}].mp4"):
                    video["video_path"] = os.path.join(video_path, filename)
                    file_exists = True
                    break
            if not file_exists:
                print(f"File with code {code} does not exist.")
            
    with open('json_file_path', 'w') as file:
        json.dump(data, file, indent=4)

# Call the function and print the result for verification
save_video_paths()
