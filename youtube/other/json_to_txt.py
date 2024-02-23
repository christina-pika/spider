import json

# Define the path to the input JSON file and the output TXT file
json_file_path = '/Users/christina/Desktop/spider/youtube/video.json' 
txt_file_path = '/Users/christina/Desktop/spider/youtube/video.txt'

# Open and load the JSON file
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

print(data['DONE'][0]['Youtube / Adobe Stock Link'])

# Extract the Youtube / Adobe Stock Link from each element and append it to the TXT file
 # Change mode to 'a' for append
for unit in data["DONE"]:
    with open(txt_file_path, 'a') as txt_file:
        if 'Youtube / Adobe Stock Link' in unit:  # Check if the key exists
            youtube_link = unit['Youtube / Adobe Stock Link']
            txt_file.write(youtube_link + '\n')
