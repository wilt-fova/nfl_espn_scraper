
# NFL ESPN Scraper

The purpose of this repository is to scrape NFL data from ESPN and load it into pandas dataframes.

## Introduction

The scraping tool is designed to provide an easy, free way to extract and clean individual game data for the following positions: 
- Quarterback
- Running Back
- Wide Receiver
- Tight End
- Kicker

In addition to game data, the birthdate of the player is scraped and used to calculate age by game. 

## Installation

Use the package manager pip to install nfl_espn_scraper.

```markdown
pip install nfl_espn_scraper
```

## Testing Suite

This repository includes a testing suite to ensure the accuracy and consistency of data processing for NFL player game logs. The suite performs two main types of tests:

1. **Specific Case Tests**  
   A set of functions test complete equality for specific players, including a running back (Christian McCaffrey), quarterback (Patrick Mahomes), and kicker (Justin Tucker). These tests verify that all games from the last five seasons for these players are being scraped and processed correctly.

2. **General Property Tests**  
   Another set of functions checks the integrity of individual stats by verifying data types, ranges, and lengths. This allows users to validate new player data, as different player datasets may vary in structure. For example, some stats might have unique formatting, such as games played in Europe, which are denoted differently in the scraped tables. If a test fails, it typically indicates that a modification is needed to handle an edge case. For instance, a player playing an international game might have a note about the location in the center of the table being scraped, as seen here: [Trevor Lawrence 2023 game log](https://www.espn.com/nfl/player/gamelog/_/id/4360310/type/nfl/year/2023).

## Usage

```markdown
import player as plyr
import pandas as pd
import test as ts
```

Select player and seasons. The first and last name do not need to be correct but the ID and position must be.
Position can be QB, RB, WR, TE, or K.
Github user mayscopeland keeps a list of player IDs here: [ESPN Player IDs](https://github.com/mayscopeland/ffb_ids).

```markdown
seasons = [2022, 2023]
first = 'Patrick'
last = 'Mahomes'
id = 3139477
position = 'QB'
```

Create Player Object

```markdown
patrick_mahomes = plyr.Player(first, last, id, position)
```

Add Seasons to Game Log

```markdown
for season in seasons:
    patrick_mahomes.Set_Season(season)
    patrick_mahomes.Set_Game_Log()
```

Get Game Log

```markdown
game_log = patrick_mahomes.Get_Game_Log()
```

Verify with General Property Tests

```markdown
test = ts.test()
test.verify_espn_pull(game_log, first, last)
```

Patrick Mahomes Game Log

```markdown

print(game_log)

       LAST    FIRST    GAME_DT    AGE    OPP     RESULT CMP ATT PASS_YDS  CMP% PASS_AVG PASS_TD INT PASS_LNG SACK    RTG   QBR CAR RUSH_YDS RUSH_AVG RUSH_TD RUSH_LNG
0   Mahomes  Patrick 2022-09-11  26.98   @ARI     W44-21  30  39      360  76.9      9.2       5   0       35    0  144.2  94.9   3        5      1.7       0        4
1   Mahomes  Patrick 2022-09-15  26.99  vsLAC     W27-24  24  35      235  68.6      6.7       2   0       41    1  106.2  66.6   2       -1     -0.5       0        0
2   Mahomes  Patrick 2022-09-25  27.02   @IND     L20-17  20  35      262  57.1      7.5       1   1       53    1   78.5  71.8   4       26      6.5       0       10
3   Mahomes  Patrick 2022-10-02  27.04    @TB     W41-31  23  37      249  62.2      6.7       3   1       36    3   97.7  90.6   4       34      8.5       0       11
4   Mahomes  Patrick 2022-10-10  27.06   vsLV     W30-29  29  43      292  67.4      6.8       4   0       36    3  117.6  65.5   4       28      7.0       0       16
5   Mahomes  Patrick 2022-10-16  27.08  vsBUF     L24-20  25  40      338  62.5      8.5       2   2       42    3   85.2  58.0   4       21      5.3       0       10
6   Mahomes  Patrick 2022-10-23  27.10    @SF     W44-23  25  34      423  73.5     12.4       3   1       57    1  132.4  91.9   0        0      0.0       0        0
7   Mahomes  Patrick 2022-11-06  27.14  vsTEN  W20-17 OT  43  68      446  63.2      6.6       1   1       33    4   80.9  72.7   6       63     10.5       1       20
8   Mahomes  Patrick 2022-11-13  27.16  vsJAX     W27-17  26  35      331  74.3      9.5       4   1       46    0  129.6  93.4   7       39      5.6       0       19
9   Mahomes  Patrick 2022-11-20  27.18   @LAC     W30-27  20  34      329  58.8      9.7       3   0       40    1  120.8  82.4   4       23      5.8       0       16
10  Mahomes  Patrick 2022-11-27  27.19  vsLAR     W26-10  27  42      320  64.3      7.6       1   1       39    0   85.4  69.6   4       36      9.0       0       13
11  Mahomes  Patrick 2022-12-04  27.21   @CIN     L27-24  16  27      223  59.3      8.3       1   0       42    2   98.2  91.5   2        9      4.5       1        6
12  Mahomes  Patrick 2022-12-11  27.23   @DEN     W34-28  28  42      352  66.7      8.4       3   3       56    2   86.6  66.9   3       -3     -1.0       0       -1
13  Mahomes  Patrick 2022-12-18  27.25   @HOU  W30-24 OT  36  41      336  87.8      8.2       2   0       21    2  117.1  93.5   5       33      6.6       1       14
14  Mahomes  Patrick 2022-12-24  27.27  vsSEA     W24-10  16  28      224  57.1      8.0       2   0       52    1  106.8  37.6   2        8      4.0       1        5
15  Mahomes  Patrick 2023-01-01  27.29  vsDEN     W27-24  29  42      328  69.1      7.8       3   1       38    0  106.1  67.2   4        8      2.0       0        4
16  Mahomes  Patrick 2023-01-07  27.31    @LV     W31-13  18  26      202  69.2      7.8       1   0       67    2  105.0  82.9   3       29      9.7       0       14
32  Mahomes  Patrick 2023-09-07  27.97  vsDET     L21-20  21  39      226  53.9      5.8       2   1       34    0   77.5  66.9   6       45      7.5       0       16
31  Mahomes  Patrick 2023-09-17  28.00   @JAX      W17-9  29  41      305  70.7      7.4       2   1       54    1   98.1  71.8   7       30      4.3       0       14
30  Mahomes  Patrick 2023-09-24  28.02  vsCHI     W41-10  24  33      272  72.7      8.2       3   0       37    0  127.3  86.3   3       28      9.3       0       15
29  Mahomes  Patrick 2023-10-01  28.04   @NYJ     W23-20  18  30      203  60.0      6.8       1   2       34    1   63.6  81.8   7       51      7.3       0       25
28  Mahomes  Patrick 2023-10-08  28.06   @MIN     W27-20  31  41      281  75.6      6.9       2   0       33    2  109.9  83.6   0        0      0.0       0        0
27  Mahomes  Patrick 2023-10-12  28.07  vsDEN      W19-8  30  40      306  75.0      7.7       1   1       40    2   94.4  66.0   6       31      5.2       0       15
26  Mahomes  Patrick 2023-10-22  28.10  vsLAC     W31-17  32  42      424  76.2     10.1       4   1       53    1  129.5  93.9   4       29      7.3       0       23
25  Mahomes  Patrick 2023-10-29  28.12   @DEN      L24-9  24  38      240  63.2      6.3       0   2       39    3   59.1  51.3   3       20      6.7       0        8
24  Mahomes  Patrick 2023-11-05  28.13  vsMIA     W21-14  20  30      185  66.7      6.2       2   0       25    2  105.6  49.2   6       24      4.0       0       16
23  Mahomes  Patrick 2023-11-20  28.18  vsPHI     L21-17  24  43      177  55.8      4.1       2   1       17    1   71.6  36.9   6       38      6.3       0       14
22  Mahomes  Patrick 2023-11-26  28.19    @LV     W31-17  27  34      298  79.4      8.8       2   0       39    1  122.8  83.7   5        9      1.8       0        7
21  Mahomes  Patrick 2023-12-03  28.21    @GB     L27-19  21  33      210  63.6      6.4       1   1       27    3   79.1  52.2   4       26      6.5       0       10
20  Mahomes  Patrick 2023-12-10  28.23  vsBUF     L20-17  25  43      271  58.1      6.3       1   1       23    1   74.9  28.9   1        8      8.0       0        8
19  Mahomes  Patrick 2023-12-17  28.25    @NE     W27-17  27  37      305  73.0      8.2       2   2       48    3   92.7  65.7   3       -5     -1.7       0       -1
18  Mahomes  Patrick 2023-12-25  28.27   vsLV     L20-14  27  44      235  61.4      5.3       1   1       45    4   73.6  32.3  10       53      5.3       0       13
17  Mahomes  Patrick 2023-12-31  28.29  vsCIN     W25-17  21  29      245  72.4      8.4       1   0       67    2  109.1  52.8   4        2      0.5       0        2
```

## Contributing

Pull requests are welcome. For any questions or support, feel free to reach out!

- Wil Maltby (https://github.com/wilt-fova)
- Email: wilmaltby0618@gmail.com
