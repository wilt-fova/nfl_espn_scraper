
# ESPN Scraper

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

Use the package manager pip to install espn_scraper.

```markdown
pip install espn_scraper
```

## Testing Suite

This repository includes a testing suite to ensure the accuracy and consistency of data processing for NFL player game logs. The suite performs two main types of tests:

1. **Specific Case Tests**  
   A set of functions test complete equality for specific players, including a running back (Christian McCaffrey), quarterback (Patrick Mahomes), and kicker (Justin Tucker). These tests verify that all games from the last five seasons for these players are being scraped and processed correctly.

2. **General Property Tests**  
   Another set of functions checks the integrity of individual stats by verifying data types, ranges, and lengths. This allows users to validate new player data, as different player datasets may vary in structure. For example, some stats might have unique formatting, such as games played in Europe, which are denoted differently in the scraped tables. If a test fails, it typically indicates that a modification is needed to handle an edge case. For instance, a player playing an international game might have a note about the location in the center of the table being scraped, as seen here: [Trevor Lawrence 2023 game log](https://www.espn.com/nfl/player/gamelog/_/id/4360310/type/nfl/year/2023).

## Usage

```markdown
import espn_scraper as espn
```

show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here
show how to use code here

## Contributing

Pull requests are welcome. For any questions or support, feel free to reach out!

- Wil Maltby (https://github.com/wilt-fova)
- Email: wilmaltby0618@gmail.com





-----------------------------------------------------

To Do's

- finish readme
- do I need init file
- Split long functions into smaller functions.
- Comment all code
