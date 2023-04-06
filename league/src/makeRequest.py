import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "RGAPI-7af1ea07-a6f1-4319-a9a5-960ec2735a49"

# Replace SUMMONER_ID with the encrypted summoner ID you want to look up
summoner_id = "QFJLaFOGjJEN5YyhqX1XBW5FpVvNGKNNflrhfKqpd-Bw-7U"
puuid= "Y9Ohd25EirbZYITMPCqOhlTta4hBy-fA9R_H1hPuia6LRTX_z0Z1Xnm_g-DQ2URSZ-E5-vcPQ-mhwg"

# Set the base URL for the API endpoint
base_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"

# Construct the full URL by appending the PUUID to the base URL
url = base_url + puuid

# Set the headers for the request
headers = {
    "X-Riot-Token": api_key
}

start = 0

# Set the optional query parameters
query_params = {
    "start": 0,
    "count": 100,  # Replace with the desired champion ID
    "type": 'ranked',  # Replace with the desired queue ID
}

# Make the request to the API
response = requests.get(url, headers=headers, params=query_params)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful, so parse the response data
    data = response.json()
    print(data)
else:
    # There was an error with the request, so print the status code and the error message
    print(url)
    print(response.headers)
    print(f"Error: {response.status_code} {response.text}")