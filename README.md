
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

1. A few functions test specific cases for complete equality. This is done for a running back (McCaffrey), quarterback (Mahomes), and kicker (Tucker). These tests check that every game over the last 5 seasons is being pulled and prepared correctly. 

2. A second set of functions are included to test that the properties of individual stats are correct. This second set is included to allow the user to verify correctness when scraping new player data as not all player data follows the same structure. 

If a new run fails to pass one of these tests, it signals to the user that an edit is likely necessary to handle the unique case. 
A common example is a player playing a game in Europe which is noted in the center of the table being scraped.
An example can be seen here: https://www.espn.com/nfl/player/gamelog/_/id/4360310/type/nfl/year/2023

## Installation

Use the package manager pip to install espn_scraper.

```markdown
pip install espn_scraper
```

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






To Do
-----------------------------------------------------

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

Classes vs. functions
---------------------

- Do not overuse classes.
- Prefer immutable data structures.
- Prefer pure functions.
