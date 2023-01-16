import requests
import time
import json
from matchlist import matchList

# Replace YOUR_API_KEY with your actual API key
api_key = "RGAPI-7af1ea07-a6f1-4319-a9a5-960ec2735a49"

# Set the base URL for the API endpoint
base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/"

# Set the headers for the request
headers = {
    "X-Riot-Token": api_key
}

# Set the list of match IDs
match_ids = matchList

# Set the delay between requests (in seconds)
delay = 120 / 99

# Iterate over the match IDs
for match_id in match_ids:
    print(f"Attempting: {match_id}.")
    # Construct the full URL by appending the match ID to the base URL
    url = base_url + str(match_id)
    # Make the request to the API
    response = requests.get(url, headers=headers)
    # Check the status code of the response
    if response.status_code == 200:
        print(f"Success, writing file.")
        # The request was successful, so parse the response data
        data = response.json()
        # Write the data to a JSON file
        with open(f"{match_id}.json", "w") as f:
            json.dump(data, f)
        print(f"File Write complete.")
    else:
        # There was an error with the request, so print the status code and the error message
        print(f"Error: {response.status_code} {response.text}")
    # Wait for the specified delay before making the next request
    time.sleep(delay)