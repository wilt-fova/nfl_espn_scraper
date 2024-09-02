from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import datetime
from utils import ls_to_matrix, calculate_age

class Player:

    def __init__(self, firstName, lastName, espn_ID, pos):

        self.firstName = firstName
        self.lastName = lastName
        self.espn_ID = espn_ID
        self.pos = pos
        self.year = None
        self.soup = None

        if (pos == 'QB'):
            self.stats_col_espn = ['LAST', 'FIRST', 'GAME_DT', 'AGE', 'OPP', 'RESULT', 
                                   'CMP', 'ATT', 'PASS_YDS', 'CMP%', 'PASS_AVG', 'PASS_TD', 
                                   'INT', 'PASS_LNG', 'SACK', 'RTG', 'QBR', 'CAR', 'RUSH_YDS', 
                                   'RUSH_AVG', 'RUSH_TD', 'RUSH_LNG']
        elif (pos == 'RB'):
            self.stats_col_espn = ['LAST', 'FIRST', 'GAME_DT', 'AGE', 'OPP', 'RESULT', 'CAR', 
                                   'RUSH_YDS', 'RUSH_AVG', 'RUSH_TD', 'RUSH_LNG', 'REC', 'TGTS', 
                                   'REC_YDS', 'REC_AVG', 'REC_TD', 'REC_LNG', 'FUM', 'LST', 'FF', 'KB']
        elif (pos == 'WR' or pos == 'TE'):
            self.stats_col_espn = ['LAST', 'FIRST', 'GAME_DT', 'AGE', 'OPP', 'RESULT', 'REC', 
                                   'TGTS', 'REC_YDS', 'REC_AVG', 'REC_TD', 'REC_LNG', 'CAR', 
                                   'RUSH_YDS', 'RUSH_AVG', 'RUSH_LNG', 'RUSH_TD', 'FUM', 'LST', 
                                   'FF', 'KB']
        elif (pos == 'K'):
            self.stats_col_espn = ['LAST', 'FIRST', 'GAME_DT', 'AGE', 'OPP', 'RESULT', '1-19', 
                                   '20-29', '30-39', '40-49', '50+', 'LNG', 'FG%', 'FG', 
                                   'AVG', 'XP', 'PTS']
        else:
            self.stats_col_espn = []
            # raise ValueError("Position must be one of the following: QB, RB, WR, TE, K")

        self.game_data = pd.DataFrame(None, columns=self.stats_col_espn)

    def Set_Year(self, year):

        # set year
        self.year = year

        # set url to scrape
        url = f'https://www.espn.com/nfl/player/gamelog/_/id/{self.espn_ID}/type/nfl/year/{self.year}'

        headers = requests.utils.default_headers()
        headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

        # send request for player data
        page = requests.get(url, headers=headers)

        self.soup = bs(page.content, features="html.parser")

    def Get_Position(self):

        position_soup = [i.text for i in self.soup.find_all(class_='PlayerHeader__Team_Info list flex pt1 pr4 min-w-0 flex-basis-0 flex-shrink flex-grow nowrap')]

        pos = ''
        if 'Quarterback' in position_soup[0]: pos = 'QB'
        elif ('Running Back' in position_soup[0]) or ('Fullback' in position_soup[0]): pos = 'RB'
        elif 'Tight End' in position_soup[0]: pos = 'TE'
        elif 'Wide Receiver' in position_soup[0]: pos = 'WR'
        elif 'Kicker' in position_soup[0]: pos = 'K'

        return pos

    def Get_Game_Data(self):

        return self.game_data

    def Set_Game_Data(self):

        # check whether the player was in the NFL during the given year
        invalid_year = [i.text for i in self.soup.find_all(class_='NoDataAvailable__Msg__Content')]
        if invalid_year == ['No available information.']: return None

        # set HTML class
        stat = [i.text for i in self.soup.find_all(class_='Table__TD')]

        # adjustments for postseason removal
        if 'Postseason' in stat: stat = stat[(stat.index('Postseason') + len(self.stats_col_espn) - 5):]

        elif ('NFC Wild Card Playoffs' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC Wild Card Playoffs') + 3):]
        elif ('NFC WILD CARD PLAYOFFS' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC WILD CARD PLAYOFFS') + 3):]

        elif ('AFC Wild Card Playoffs' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC Wild Card Playoffs') + 3):]
        elif ('AFC WILD CARD PLAYOFFS' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC WILD CARD PLAYOFFS') + 3):]
        elif ('AFC Wild Card Playoffs - originally scheduled on Jan. 14' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC Wild Card Playoffs - originally scheduled on Jan. 14') + 3):]

        elif ('NFC Divisional Playoffs' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC Divisional Playoffs') + 3):]
        elif ('NFC DIVISIONAL PLAYOFFS' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC DIVISIONAL PLAYOFFS') + 3):]

        elif ('AFC Divisional Playoffs' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC Divisional Playoffs') + 3):]
        elif ('AFC DIVISIONAL PLAYOFFS' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC DIVISIONAL PLAYOFFS') + 3):]

        elif ('AFC Championship' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC Championship') + 3):]
        elif ('AFC CHAMPIONSHIP' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('AFC CHAMPIONSHIP') + 3):]

        elif ('NFC Championship' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC Championship') + 3):]
        elif ('NFC CHAMPIONSHIP' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('NFC CHAMPIONSHIP') + 3):]

        elif ('NFC Wild Card Playoffs' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC Wild Card Playoffs') + 2):]
        elif ('NFC WILD CARD PLAYOFFS' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC WILD CARD PLAYOFFS') + 2):]

        elif ('AFC Wild Card Playoffs' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC Wild Card Playoffs') + 2):]
        elif ('AFC WILD CARD PLAYOFFS' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC WILD CARD PLAYOFFS') + 2):]

        elif ('NFC Divisional Playoffs' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC Divisional Playoffs') + 2):]
        elif ('NFC DIVISIONAL PLAYOFFS' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC DIVISIONAL PLAYOFFS') + 2):]

        elif ('AFC Divisional Playoffs' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC Divisional Playoffs') + 2):]
        elif ('AFC DIVISIONAL PLAYOFFS' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC DIVISIONAL PLAYOFFS') + 2):]

        elif ('AFC Championship' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC Championship') + 2):]
        elif ('AFC CHAMPIONSHIP' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('AFC CHAMPIONSHIP') + 2):]

        elif ('NFC Championship' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC Championship') + 2):]
        elif ('NFC CHAMPIONSHIP' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('NFC CHAMPIONSHIP') + 2):]

        elif ('Pro Bowl' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('Pro Bowl') + 2):]
        elif ('Pro Bowl' in stat) and (self.pos == 'K') and (self.year == 2021): stat = stat[(stat.index('Pro Bowl') + 2):]
        elif ('Pro Bowl' in stat): stat = stat[(stat.index('Pro Bowl') + 3):]
        elif ('PRO BOWL' in stat): stat = stat[(stat.index('PRO BOWL') + 3):]
        elif ('Pro Bowl Games' in stat) and (self.pos == 'QB'): stat = stat[(stat.index('Pro Bowl Games') + 2):]
        elif ('Pro Bowl Games' in stat) and (self.pos != 'QB'): stat = stat[(stat.index('Pro Bowl Games') + 3):]

        # adjustments for europe games
        offset = 2
        if (self.pos != 'QB') and (self.pos != 'K'): offset = 3

        if ('NFL Frankfurt Games' in stat):
            remove = stat.index('NFL Frankfurt Games')
            del stat[remove:(remove + offset)]
        if ('NFL London Games' in stat): 
            remove = stat.index('NFL London Games')
            del stat[remove:(remove + offset)]
        if ('NFL London Games' in stat): 
            remove = stat.index('NFL London Games')
            del stat[remove:(remove + offset)]
        
        # find and adjust for any team changes during season
        condition = lambda x: x[:10] == 'Previously'
        stat = [x for x in stat if len(x) < 11 or not condition(x)]

        # convert ls of strings to matrix of strings
        matrix = ls_to_matrix(stat, len(self.stats_col_espn) - 3)
        matrix = matrix[:len(matrix)-3]

        # add game_dt column
        for ls in matrix:
            
            month = int(ls[0][4:].split("/")[0])
            day = int(ls[0][4:].split("/")[1])
            year = self.year
            if month in [1,2]: year = year + 1

            game_dt = datetime.datetime(year, month, day)
            age = self.Get_Age(game_dt)

            ls[0] = game_dt
            ls.insert(1, age)

        # add name columns
        for ls in matrix:
            ls.insert(0, self.firstName)
            ls.insert(0, self.lastName)

        # create pandas dataframe
        df = pd.DataFrame(matrix, columns=self.stats_col_espn)

        # replace dashes with zero
        for key in self.stats_col_espn:
            for i in range(len(df[key])):
                if df[key][i] == '-':
                    df[key][i] = '0'

        # set scraped player data
        self.game_data = pd.concat([self.game_data, df], ignore_index=True)

    def Get_Age(self, dt):

        # set HTML class based on position
        soup = [i.text for i in self.soup.find_all(class_='fw-medium clr-black')]
        date_index = 1 - int(soup[0].find("/") != -1)

        # get birth date from html string
        split_string = soup[date_index].split('/')
        month = split_string[0]
        day = split_string[1]
        year = split_string[2][:4]
        birthdate = datetime.datetime(int(year), int(month), int(day))

        # set age variable
        return calculate_age(birthdate, dt)
