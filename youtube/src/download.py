import json
import os

set_file_path = os.path.join(os.path.dirname(__file__), '..', 'set.json')
with open(set_file_path, 'r') as set_file:
    settings = json.load(set_file)

json_file_path = settings["json_file_path"]

with open(json_file_path, 'r') as file:
    data = json.load(file)

# Iterate through each element in the JSON data
for ele in data:
    # Check if the "Youtube / Adobe Stock Link" is not empty
    if ele["Youtube / Adobe Stock Link"] != "":
        # Construct the command
        command = f'yt-dlp --format-sort res {ele["Youtube / Adobe Stock Link"]} --concurrent-fragments 5'
        ele["video_path"] = ele["Youtube / Adobe Stock Link"].split('=')[-1]
        # Execute the command
        os.system(command)