import sources.espn_data as espn
import data_eng.write as sql
import pandas as pd
import data_eng.test as ts

run new player list for 5 years ... 2019 - 2023
add your own player ID

df = pd.read_csv("sources/players_new.csv")
year = 2019
for i in range(0,131):

    # Get Player
    firstName = df['first_name'][i]
    lastName = df['last_name'][i]
    position = df['pos'][i]
    print("Player: " + firstName + " " + lastName + " " + str(i))

    # Get Game Log
    plyr = espn.player(firstName, lastName, df['espn_id'][i], position)
    plyr.Set_Year(year)
    plyr.Set_Soup()
    plyr.Set_Game_Data()
    data = plyr.Get_Game_Data()

    # Test & Load
    if position == 'QB':
        ts.test().test_espn_quarterback(data, firstName, lastName)
        sql.add_rows_quarterback(data)
    elif position == 'K':
        ts.test().test_espn_kicker(data, firstName, lastName)
        sql.add_rows_kicker(data)
    else:
        ts.test().test_espn_flex(data, firstName, lastName)
        sql.add_rows_flex(data, position)

