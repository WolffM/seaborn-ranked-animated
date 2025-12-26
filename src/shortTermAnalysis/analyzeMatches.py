import pandas as pd
import json
import os

MY_RIOT_ID = "Hadoku"  # Replace with your 'riotIdGameName'
MY_PUUID = "Y9Ohd25EirbZYITMPCqOhlTta4hBy-fA9R_H1hPuia6LRTX_z0Z1Xnm_g-DQ2URSZ-E5-vcPQ-mhwg"

def process_match(file_path):
    with open(file_path, 'r') as f:
        match_data = json.load(f)
    game_data = {}
    # Match-level data (add the gameMode check)
    if match_data['info']['gameMode'] == 'CLASSIC':  # Filter here
        game_data = {
            "gameVersion": match_data['info']['gameVersion'],
            "gameType": match_data['info']['gameType'],
            "gameMode": match_data['info']['gameMode'],
            "gameId": match_data['info']['gameId']
        }
    else:
        return

     # Find your participant data
    for participant in match_data['info']['participants']:
        if participant['riotIdGameName'] == MY_RIOT_ID or participant['puuid'] == MY_PUUID:
            my_data = participant
            break  # Exit loop once we found our participant

    # Extract specific participant stats
    game_data.update({
        "championName": my_data['championName'],
        "damageDealtToObjectives": my_data['damageDealtToObjectives'],
        "damageDealtToTurrets": my_data['damageDealtToTurrets'],
        "totalDamageDealtToChampions": my_data['totalDamageDealtToChampions'],
        "win":  my_data['win'],
        "kills": my_data['kills'],
        "deaths": my_data['deaths'],
        "assists": my_data['assists']
    })

    assert isinstance(my_data, dict)  # Assert that it's a dictionary type
    if 'challenges' in my_data:
        game_data.update({
            "damagePerMinute": my_data['challenges'].get('damagePerMinute', None),
            "kda": my_data['challenges'].get('kda', None),
            "killParticipation": my_data['challenges'].get('killParticipation', None),
        })

    return game_data


# Main Processing
all_data = []
matches_dir = 'matches' 

for filename in os.listdir(matches_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(matches_dir, filename)
        match_data = process_match(filepath)  # Get potential match data
        if match_data:  # Only append if we get valid match data
            all_data.append(match_data)

# Create CSV (Only if you have collected some valid data)
if all_data: 
    df = pd.DataFrame(all_data)
    df.to_csv('match_stats.csv', index=False)
else:
    print("No 'CLASSIC' game mode matches found in the directory")