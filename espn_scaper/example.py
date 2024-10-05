import espn_data as espn
import pandas as pd

# Select Player & Seasons
df = pd.read_csv("players.csv")
seasons = [2021, 2022, 2023]
csv_index = 0

# Create Player Object
patrick_mahomes = espn.Player(df['first_name'][csv_index], 
                              df['last_name'][csv_index], 
                              df['espn_id'][csv_index], 
                              df['pos'][csv_index])

# Add Seasons to Game Log
for season in seasons:
    patrick_mahomes.Set_Season(season)
    patrick_mahomes.Set_Game_Log()

# View Game Log
print(patrick_mahomes.Get_Game_Log())
