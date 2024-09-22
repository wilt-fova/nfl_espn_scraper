import espn_data as espn
import pandas as pd

# Select Player & Seasons
df = pd.read_csv("players.csv")
years = [2021, 2022, 2023]
plyr_index = 17

# Create Player Object
plyr = espn.Player(df['first_name'][plyr_index], 
                   df['last_name'][plyr_index], 
                   df['espn_id'][plyr_index], 
                   df['pos'][plyr_index])

# Set Game Data
for year in years:
    plyr.Set_Year(year)
    plyr.Set_Game_Data()
    stats_df = plyr.Get_Game_Data()

# View Game Data
print(stats_df)
