import csv
import json
import os

set_file_path = os.path.join(os.path.dirname(__file__), '..', 'set.json')
with open(set_file_path, 'r') as set_file:
    settings = json.load(set_file)

# Apply the settings from set.json
csv_file_path = settings["csv_file_path"]
json_file_path = csv_file_path.replace('.csv', '.json')
settings["json_file_path"] = json_file_path
settings["video_path"] = os.path.join(os.path.dirname(__file__), '..', 'video')

with open(set_file_path, 'w') as set_file:
    settings = json.load(set_file)
    json.dump(settings, set_file, indent=4)

def csv_to_json(csv_file_path, json_file_path):
    # Create an empty list to store the rows as dictionaries
    data = []
    
    # Open the CSV file for reading
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        # Use the csv.DictReader to read the CSV file into a dictionary
        csv_reader = csv.DictReader(csv_file)
        
        # Loop through each row in the csv_reader
        for row in csv_reader:
            # Append each row(dictionary) to the data list
            data.append(row)
    
    # Open the JSON file for writing
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        # Use json.dump to write the data list (which now contains dictionaries) to the JSON file
        json.dump(data, json_file, indent=4)

csv_to_json(csv_file_path, json_file_path)
