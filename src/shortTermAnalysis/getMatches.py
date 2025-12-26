import requests
import json
import logging  # Add logging

logging.basicConfig(filename='match_retrieval.log', level=logging.DEBUG) # Log to file


# Replace YOUR_API_KEY with your actual API key
API_KEY = "RGAPI-1a385bd5-58b2-40a3-926a-17afd739ec70"

# Constants 
BASE_URL = "https://americas.api.riotgames.com/lol/match/v5/matches/"
BASE_URL_v4 = "https://americas.api.riotgames.com/lol/match/v5/matches/"
MATCHLIST_ENDPOINT = "by-puuid/{}/ids"  # Requires your PUUID

# Get your PUUID (visit https://developer.riotgames.com/ if you need help finding it)
puuid = "Y9Ohd25EirbZYITMPCqOhlTta4hBy-fA9R_H1hPuia6LRTX_z0Z1Xnm_g-DQ2URSZ-E5-vcPQ-mhwg"

headers = {
    "X-Riot-Token": API_KEY
}

def get_matchlist(puuid, start=0, count=100):
    """Retrieves a list of match IDs for the given PUUID."""
    url = BASE_URL + MATCHLIST_ENDPOINT.format(puuid)
    params = {"start": start, "count": count}  
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        pushMatchList(response.json())
    else:
        print(f"Error retrieving matchlist: {response.status_code}")
        return None

def get_match_details(match_id):
    """Fetches detailed match data for a given match ID."""
    url = BASE_URL + match_id
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        logging.debug(f"Success (200) for match_id: {match_id}, Response: {response.content}")
        return response.json()
    else:
        print(f"Error retrieving match details: {response.status_code}")
        logging.error(f"Error (status: {response.status_code}) for match_id: {match_id},  Response: {response.content}")
        return None

def pushMatchList(match_list):
    for match_id in match_list[:100]:  
        match_details = get_match_details(match_id)

        # Create a filename for the current match
        filename = f"matches/{match_id}.json"

        with open(filename, 'w') as outfile:
            json.dump(match_details, outfile) 
    else:
        print(f"Failed to get match list for PUUID: {puuid}")

match_list = get_matchlist(puuid, start=100, count=100)