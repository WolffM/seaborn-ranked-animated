import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "RGAPI-7af1ea07-a6f1-4319-a9a5-960ec2735a49"

# Replace SUMMONER_NAME with the summoner name you want to look up
summoner_name = "Hadoku"

# Set the base URL for the API endpoint
base_url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"

# Construct the full URL by appending the summoner name to the base URL
url = base_url + summoner_name

# Set the headers for the request
headers = {
    "X-Riot-Token": api_key
}

# Make the request to the API
response = requests.get(url, headers=headers)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful, so parse the response data
    data = response.json()
    # Print the encrypted summoner ID
    print(data["id"])
else:
    # There was an error with the request, so print the status code and the error message
    print(f"Error: {response.status_code} {response.text}")