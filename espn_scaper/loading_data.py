import espn_data as espn
import pandas as pd

# Select Player
df = pd.read_csv("players.csv")
years = [2019, 2020, 2021, 2022, 2023]
plyr_index = 566

# Get Game Log
plyr = espn.Player(df['first_name'][plyr_index], 
                   df['last_name'][plyr_index], 
                   df['espn_id'][plyr_index], 
                   df['pos'][plyr_index])

for year in years:
    plyr.Set_Year(year)
    plyr.Set_Game_Data()
    stats_df = plyr.Get_Game_Data()

arrays = [row.to_numpy() for _, row in stats_df.iterrows()]
for array in arrays:
    print(list(array))
