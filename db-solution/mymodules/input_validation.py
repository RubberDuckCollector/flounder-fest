import re
import sys
from datetime import datetime

"""
variables starting with `p_` denote a parameter.
the error cases are nearly always checked first, making the code quick to read.
"""

def validate_start_id(p_start_id: int):
    if not isinstance(p_start_id, int):
        print("Please enter an integer.")
        sys.exit(0)
    elif p_start_id < 0:
        print("Please enter an integer of 0 or more.")
        sys.exit(0)
    else:
        pass


def validate_season(p_season: int):
    if not isinstance(p_season, int):
        print("Please enter an integer.")
        sys.exit(0)
    elif p_season < 0:
        print("Please enter an integer of 0 or more.")
        sys.exit(0)
    else:
        pass


def validate_episode(p_episode: int):
    if not isinstance(p_episode, int):
        print("Please enter an integer.")
        sys.exit(0)
    elif p_episode < 0:
        print("Please enter an integer of 0 or more.")
        sys.exit(0)
    else:
        pass


def validate_final_episode_of_season(p_is_final_episode_of_season: int) -> bool:
    match p_is_final_episode_of_season:
        case 1:
            p_is_final_episode_of_season = True
        case 2:
            p_is_final_episode_of_season = False
        case _:
            print("Enter a valid number (1 or 2).")
            sys.exit(0)

    return p_is_final_episode_of_season

"""
As you can see from here and below, the regexes are matched with single quotes.
SQL requires them for dates and text.
the `main-db.py` program adds quotes to the user inputs, so the user doesn't have to add the quotes.
this would mean if they do add quotes, there would be 2 layers of quotes and it would cause an error.
"""

def validate_date(p_date: str):
    date_regex = r"^'\d{4}-\d{2}-\d{2}'$"
    if re.match(date_regex, p_date):
        pass
    else:
        print("Please enter a date in the format YYYY-MM-DD.")
        sys.exit(0)
    try:
        # test that `date` is a valid date
        datetime.strptime(p_date, "'%Y-%m-%d'")  # the ' chars make it work with SQL's syntax needing ' on dates and text
    except ValueError:
        print("Please enter a valid date.")
        sys.exit(0)


def validate_tiebreak_episode(p_is_tiebreak_episode: int) -> bool:
    match p_is_tiebreak_episode:
        case 1:
            p_is_tiebreak_episode = True
        case 2:
            p_is_tiebreak_episode = False
        case _:
            print("Enter a valid number (1 or 2).")
            sys.exit(0)

    return p_is_tiebreak_episode


def validate_youtube_title(p_title: str):
    title_pattern = r"^'(.*)'$"
    if not re.match(title_pattern, p_title):
        print("Please enter a valid youtube link.")
        sys.exit(0)
    else:
        pass

def validate_youtube_link(p_link: str):
    # the ' chars make it work with SQL's syntax needing ' on dates and text
    link_pattern = r"^'(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=|playlist\?list=|channel/|c/)?[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=-]*)*'$"
    if not re.match(link_pattern, p_link):
        print("Please enter a valid youtube link.")
        sys.exit(0)
    else:
        pass


def validate_num_races(p_num_races: int):
    if p_num_races < 0:
        print("Please enter an integer of 0 or more.")
        sys.exit(0)
    else:
        pass


def validate_num_item_or_dodge(p_num_item_or_dodge: int):
    if p_num_item_or_dodge < 0:
        print("Please enter an integer of 0 or more.")
    else:
        pass


def validate_nmeade_win(p_nmeade_win: int) -> bool:
    match p_nmeade_win:
        case 1:
            p_nmeade_win = True
        case 2:
            p_nmeade_win = False
        case _:
            print("Enter a valid number (1 or 2).")
            sys.exit(0)

    return p_nmeade_win
