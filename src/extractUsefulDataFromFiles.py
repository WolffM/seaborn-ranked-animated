import os
import json

# Set the path to the folder containing the JSON files
folder_path = "league\Assets\Hadoku\match"

# Iterate over the files in the folder
for file_name in os.listdir(folder_path):
    # Check if the file is a JSON file
    if file_name.endswith(".json"):
        # Construct the full path to the file
        file_path = os.path.join(folder_path, file_name)
        # Open the file and read the contents
        with open(file_path, "r") as f:
            data = json.load(f)
        # Retrieve the desired value from the data
        value = data["key"]
        # Do something with the value
        print(value)