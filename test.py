import unittest
import datetime
import pandas as pd

class test(unittest.TestCase):

    def test_espn(self, df, firstName, lastName):

        for item in df['LAST']: self.assertTrue(item == lastName)
        
        for item in df['FIRST']: self.assertTrue(item == firstName)

        for item in df['GAME_DT']:
            self.assertTrue(isinstance(item, pd.Timestamp))

        last_age = 100
        for item in df['AGE']:
            self.assertTrue(item > 19)         # Youngest NFL Player
            self.assertTrue(item < 46)         # Oldest NFL Player
            self.assertTrue(item <= last_age)   # Descending Age
            last_age = item

        for item in df['OPP']:
            self.assertTrue(item[0] == '@' or item[:2] == 'vs')
            self.assertFalse(item.isnumeric())

        for item in df['RESULT']:
            self.assertTrue(item[0] == 'W' or item[0] == 'L' or item[0] == 'T')

    def test_espn_quarterback(self, df, firstName, lastName):

        self.test_espn(df, firstName, lastName)

        numeric_stats = ['CMP', 'ATT', 'PASS_YDS', 'PASS_TD', 'INT', 'PASS_LNG', 'SACK', 'CAR', 'RUSH_YDS', 'RUSH_TD', 'RUSH_LNG']
        for stat in numeric_stats:
            for item in df[stat]:
                self.assertTrue(item.isnumeric() or item[1:].isnumeric())

        numeric_stats = ['CMP%', 'PASS_AVG', 'RTG', 'QBR', 'RUSH_AVG']
        for stat in numeric_stats:
            for item in df[stat]:
                self.assertTrue(item[0].isnumeric() or item[1].isnumeric())
                
        print('Passed')

    def test_espn_flex(self, df, firstName, lastName):

        self.test_espn(df, firstName, lastName)

        numeric_stats = ['CAR', 'RUSH_YDS', 'RUSH_TD', 'RUSH_LNG', 'REC', 'TGTS', 'REC_YDS', 'REC_TD', 'REC_LNG', 'FUM', 'LST', 'FF', 'KB']
        for stat in numeric_stats:
            for item in df[stat]:
                self.assertTrue(item.isnumeric() or item[1:].isnumeric())

        numeric_stats = ['RUSH_AVG', 'REC_AVG']
        for stat in numeric_stats:
            for item in df[stat]:
                self.assertTrue(item[0].isnumeric() or item[1].isnumeric())

        print('Passed')

    def test_espn_kicker(self, df, firstName, lastName):

        self.test_espn(df, firstName, lastName)

        dist_stats = ['1-19', '20-29', '30-39', '40-49', '50+', 'FG', 'XP']
        for stat in dist_stats:
            for item in df[stat]:
                self.assertTrue(item[0].isnumeric())
                self.assertTrue((item[1] == '-' and item[2].isnumeric()) or 
                                (item[2] == '-' and item[3].isnumeric() and item[4].isnumeric()))

        numeric_stats = ['LNG', 'AVG', 'PTS']
        for stat in numeric_stats:
            for item in df[stat]:
                self.assertTrue(item.isnumeric())
        
        for item in df['FG%']:
            self.assertTrue(item[0].isnumeric() and item[-1].isnumeric() and item[-2] == '.')

        print('Passed')

if __name__ == '__main__':
    unittest.main()
