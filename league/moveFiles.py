import os
import json
import csv
from datetime import datetime
from ex import basePath, rankedPath, rankedPath2022, myPIIDs, src_folder, dst_folder, csvFileName

#             0         1         2          3          4         5       6         7          8             9                 10              11        12        13          14
headers = ['GameId', 'Date', 'Duration', 'TeamId', 'Champion', 'Role', 'Kills', 'Assists', 'Deaths', 'LongestTimeAlive', 'TotalHealing', 'WardsKilled', 'Win', 'TotalLp', 'CurrentRank']
patchDates = ['2022-01-11', '2022-01-25', '2022-02-08', '2022-02-23', '2022-03-08', '2022-03-22', '2022-04-05', '2022-04-19', '2022-05-03', '2022-05-17', '2022-06-01', '2022-06-14', '2022-06-28', '2022-07-19', '2022-08-02', '2022-08-16', '2022-08-30', '2022-09-13', '2022-09-27', '2022-10-11', '2022-10-25', '2022-11-08', '2022-11-21', '2022-12-06']
dateformatRiot = f'%Y-%m-%d %H:%M:%S'
dateformatPatch = f'%Y-%m-%d'

def moveRankedMatches():
    # Iterate over the files in the source folder
    for file_name in os.listdir(src_folder):
        # Check if the file is a JSON file
        if file_name.endswith(".json"):
            # Construct the full path to the file
            file_path = os.path.join(src_folder, file_name)
            # Open the file and read the contents
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Check the value of the desired key
            if "info" in data:
                if data["info"]["queueId"] == 420:
                    # The value matches, so move the file to the destination folder
                    os.rename(file_path, os.path.join(dst_folder, file_name))
            else:
                if data["queueId"] == 420:
                    # The value matches, so move the file to the destination folder
                    os.rename(file_path, os.path.join(dst_folder, file_name))
def moveMatches2022():
        # Iterate over the files in the source folder
    for file_name in os.listdir(src_folder):
        # Check if the file is a JSON file
        if file_name.endswith(".json"):
            # Construct the full path to the file
            file_path = os.path.join(src_folder, file_name)
            # Open the file and read the contents
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # Check the value of the desired key
            if "info" in data:
                if data["info"]["gameVersion"].startswith('12.'):
                    if(not(data["info"]["gameVersion"].startswith('12.22') or data["info"]["gameVersion"].startswith('12.23'))):
                        # The value matches, so move the file to the destination folder
                        os.rename(file_path, os.path.join(dst_folder, file_name))
            else:
                if data["gameVersion"].startswith('12.'):
                    if(not(data["gameVersion"].startswith('12.22') or data["gameVersion"].startswith('12.23'))):
                        # The value matches, so move the file to the destination folder
                        os.rename(file_path, os.path.join(dst_folder, file_name))
def removeInfo():
    # Iterate over the files in the source folder
    for file_name in os.listdir(src_folder):
        # Check if the file is a JSON file
        if file_name.endswith(".json"):
            # Construct the full path to the file
            file_path = os.path.join(src_folder, file_name)
            # Open the file and read the contents
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            f.close()
        if "info" in data:
            for key, value in data["info"].items():
                data[key] = value
            del data["info"]
            print(f"Removed info from: {file_name}.")

                # Encode the modified object as a JSON string
            json_data = json.dumps(data)

            # Open the file in write mode
            with open(file_path, "w", encoding="utf-8") as g:
                # Write the JSON string to the file
                g.write(json_data)
                print(f"Wrote data to: {file_path}.")
            g.close()
def writeDataToCSV():
    # Initialize an empty list to store the data
    print(f"Starting writeDataToCSV.")
    print(f"Source Folder: {src_folder}")
    writer = csv.writer(open("output.csv", "w", newline=""))
    writer.writerow(headers)
    gameId = 0
    # Iterate over the files in the source folder
    for file_name in os.listdir(src_folder):
        # Check if the file is a JSON file
        if file_name.endswith(".json"):
            # Construct the full path to the file
            file_path = os.path.join(src_folder, file_name)
            # Open the file and read the contents
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            date = datetime.fromtimestamp(data['gameCreation'] / 1000).strftime(dateformatRiot)
            duration = data['gameDuration']
            gameId+=1
            # Check the condition on the object
            for player in data["participants"]:
                if(player["summonerName"] == "Hadoku"):
                    teamId = player["teamId"]
                    deaths = player["deaths"]
                    assists = player["assists"]
                    kills = player["kills"]
                    role = player["role"]
                    lane = player["lane"]
                    longestTimeSpentLiving = player["longestTimeSpentLiving"]
                    totalHeal = player["totalHeal"]
                    wardsKilled = player["wardsKilled"]
                    win = player["win"]
                    championName = player['championName']

                    position = ""
                    if((championName == 'Xayah' or championName == 'Sivir') or (role=="CARRY" and lane =="BOTTOM")):
                        position = "Bottom"
                    elif((role=="SOLO" and lane =="MIDDLE") or (role=="DUO" and lane =="MIDDLE")):
                        position = "Middle"
                    elif((role=="SUPPORT" and lane =="BOTTOM") or (role=="SUPPORT" and lane =="NONE") or (role=="SUPPORT" and lane =="MIDDLE") or (role=="DUO" and lane =="NONE") or (role=="SUPPORT" and lane =="TOP") or (role=="DUO" and lane =="BOTTOM") or (role=="SOLO" and lane =="BOTTOM")):
                        position = "Support"
                    elif(role=="NONE" and lane =="JUNGLE"):
                        position = "Jungle"                    
                    else:
                        print(f"What is: {championName} {role} {lane}")

                    row=[gameId*2, date, duration, teamId, championName, position, kills, assists, deaths, longestTimeSpentLiving, totalHeal, wardsKilled, win]
                    writer.writerow(row)
                    break
def readCSV():
    # Open the CSV file
    data = ""
    with open(csvFileName) as f:
        # Create a CSV reader object
        reader = csv.reader(f)
        next(reader)
        data = list(reader)

        patchResults = []

        # Initialize the sum
        totalLp = 301
        totalLpGraph = 301
        patchLp = 0
        rankLp = 301
        divsionLp = 1
        currentDivision = 1
        currentRank = 1
        currentGameCount = 0
        totalGameCount = 0
        currentPatch = 0
        patchStartX = 0
        patchGamesPlayed = 0

        prev_row = None
        # Iterate over the rows in the CSV file
        for row in data:
            currentGameCount+=1
            totalGameCount+=1
            patchGamesPlayed+=1

            if row[12] == "True":
                divsionLp+=15
                totalLpGraph+=15
                rankLp+=15
                totalLp+=15
                patchLp+=15
                if(rankLp >= 400):
                    currentDivision = 4
                    divsionLp = rankLp-400
                    rankLp = rankLp-400
                    currentRank+=1
                    #print(f"Upgraded Rank!!! now: {currentRank}.{currentDivision}")
                    #print(f"This took: {currentGameCount} games.\n")
                    currentGameCount = 0
                elif(divsionLp >= 100):
                    divsionLp = divsionLp-100
                    currentDivision-=1
                    #print(f"Upgraded Divison! now: {currentRank}.{currentDivision}")
            else:
                divsionLp-=15
                rankLp-=15
                totalLp-=15
                patchLp-=15
                if((totalLp+15 >= 400) and (totalLp+15 < 415)):
                    totalLpGraph = 400
                elif((totalLp+15 >= 800) and (totalLp+15 < 815)):
                    totalLpGraph = 800
                elif((totalLp+15 >= 1200) and (totalLp+15 < 1215)):
                    totalLpGraph = 1200
                else:
                    totalLpGraph-=15
                if(rankLp < -30):
                    totalLpGraph = totalLp
                    currentDivision = 1
                    divsionLp = 100+rankLp
                    rankLp = 400+rankLp
                    currentRank-=1
                    #print(f"Dropped Rank..... now: {currentRank}.{currentDivision}")
                    #print(f"This took: {currentGameCount} games.\n")
                    currentGameCount = 0
                elif(divsionLp < 0 and rankLp > 0):
                    currentDivision+=1
                    divsionLp = 100+divsionLp
                    #print(f"Dropped Divison... now: {currentRank}.{currentDivision}")
            if datetime.strptime(row[1], dateformatRiot).date() > datetime.strptime(patchDates[currentPatch], dateformatPatch).date():
                patchResults.append({'PatchName':f'13.{currentPatch}', 'Start':int(patchStartX), 'End':int(row[0])-1, 'LpChange':patchLp, 'GamesPlayed':patchGamesPlayed})
                currentPatch+=1
                patchGamesPlayed = 0
                patchLp = 0
                patchStartX = row[0]


            row.append(totalLpGraph)
            row.append(f"{currentRank}.{currentDivision}")

        print(f"Total lp:{totalLpGraph}")
    with open("output2.csv", "w", newline="") as g:
        writer = csv.writer(g)
        for row in data:
            writer.writerow(row)
    with open("patchResults.json", "w") as k:
        json.dump(patchResults, k)
            
#if(not(prev_row == None)):

#prev_row = row