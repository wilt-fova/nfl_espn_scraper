
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

## Testing Suite Overview

This repository includes a testing suite to ensure the accuracy and consistency of data processing for NFL player game logs. The suite performs two main types of tests:

1. **Specific Case Tests**  
   A set of functions test complete equality for specific players, including a running back (Christian McCaffrey), quarterback (Patrick Mahomes), and kicker (Justin Tucker). These tests verify that all games from the last five seasons for these players are being scraped and processed correctly.

2. **General Property Tests**  
   Another set of functions checks the integrity of individual stats by verifying data types, ranges, and lengths. This allows users to validate new player data, as different player datasets may vary in structure. For example, some stats might have unique formatting, such as games played in Europe, which are denoted differently in the scraped tables. If a test fails, it typically indicates that a modification is needed to handle an edge case. For instance, a player playing an international game might have a note about the location in the center of the table being scraped, as seen here: [Mahomes' 2023 game log](https://www.espn.com/nfl/player/gamelog/_/id/4360310/type/nfl/year/2023).

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

Pull requests are welcome. Feel free to reach out!

## Contact

For any questions or support, please contact:

- Wil Maltby (https://github.com/wilt-fova)
- Email: wilmaltby0618@gmail.com





-----------------------------------------------------

To Do's

- finish readme

- do I need init file
- check all other files
- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- Functions should do one thing and one thing only.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules under ``somepackage/`` using ``from .somemodule import something``.
- Do file I/O on the "outside" of your code, not deep inside.
- Modularise everything you can. I tend to do 'themed' modules, some people do basically a module per function.
- Don't use different folders unless your project is getting really, really big
- Stick to one casing format (case_it, caseIt, CaseIt etc.)
- Decide if you're going to have something to denote module only functions (most people use _fuction or _foo to differentiate it)
- Comment all code
- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.
