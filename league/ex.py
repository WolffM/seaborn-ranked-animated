# Replace YOUR_API_KEY with your actual API key
api_key = "RGAPI-7af1ea07-a6f1-4319-a9a5-960ec2735a49"

# Replace SUMMONER_NAME with the summoner name you want to look up
summoner_name = "Hadoku"

# Set the paths to the source and destination folders
basePath = "../league/Hadoku/match"
rankedPath = "../league/Hadoku/rankedMatches"
rankedPath2022 = "../league/Hadoku/rankedMatches2022"

csvFileName = "output.csv"

#Find your own PIIDs
myPIIDs = [
    "BzN1fLk5kfMK8RHIb-Y7I7_xiPIuLI_fJu7cGzfF2nxyD1AYxQnCSTWgaEzQ-taOXicq2RnEzv252g",
    "Y9Ohd25EirbZYITMPCqOhlTta4hBy-fA9R_H1hPuia6LRTX_z0Z1Xnm_g-DQ2URSZ-E5-vcPQ-mhwg",
    "sMpeHpMlu54PKWbTh-ydKAIZeKEb88C7VQth_Ash4EQCRD8x94eG0H4lQV42weXk6C-Iy22kOfRO2w"
]

src_folder = rankedPath2022
dst_folder = ""