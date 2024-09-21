
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

A testing suite is included to check code in two ways. 

1. A few functions test specific cases for complete equality. This is done for a running back (McCaffrey), quarterback (Mahomes), and kicker (Tucker).
    These tests check that every game over the last 5 seasons is being pulled and prepared correctly. 

2. A second set of functions are included to test that the properties of individual stats are correct. 
This second set is included to allow the user to verify correctness when scraping new player data as not all player data follows the same structure. 
If some new player failed to pass one of these tests, it allowed me to quickly write new rules to handle the unique case. 
A common example is a player playing a game in Europe which is noted in the center of the table being scraped. 
An example can be seen here: https://www.espn.com/nfl/player/gamelog/_/id/4360310/type/nfl/year/2023

## Installation

Use the package manager pip to install nfl_data_py.

`pip install espn_scraper`

## Usage
To use MyProject, run the following command:

```bash
python myproject.py --option value

## Contributing
We welcome contributions to MyProject. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Submit a pull request.

## Contact
For any questions or support, please contact:

- Wil Maltby (https://github.com/wilt-fova)
- Email: wilmaltby0618@gmail.com






Split your code into packages, modules, and functions
-----------------------------------------------------

- All code should be inside some function (except perhaps ``if __name__ == '__main__':``).
- Split long functions into smaller functions.
- If you need to scroll through a function over several screens, it is probably too long.
- Functions should do one thing and one thing only.
- Hide internals with underscores.
- Organize related functions into modules.
- If modules grow too large, split them.
- Import from other modules under ``somepackage/`` using ``from .somemodule import something``.
- Do file I/O on the "outside" of your code, not deep inside.


Classes vs. functions
---------------------

- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.





