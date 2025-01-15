import re
import sys
from datetime import datetime

"""
variables starting with `p_` denote a parameter.
"""

def validate_start_id(p_start_id: int):
    if p_start_id > 0:
        pass
    else:
        print("Please enter a positive integer.")
        sys.exit(0)


def validate_season(p_season: int):
    if p_season > 0:
        pass
    else:
        print("Please enter a positive integer.")
        sys.exit(0)


def validate_episode(p_episode: int):
    if p_episode > 0:
        pass
    else:
        print("Please enter a positive integer.")
        sys.exit(0)


def validate_final_episode_of_season(p_is_final_episode_of_season: int):
    match p_is_final_episode_of_season:
        case 1:
            p_is_final_episode_of_season = True
        case 2:
            p_is_final_episode_of_season = False
        case _:
            print("Enter a valid number (1 or 2).")
            sys.exit(0)


def validate_date(p_date: str):
    date_regex = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(date_regex, p_date):
        pass
    else:
        print("Please enter the date in the format YYYY-MM-DD.")
        sys.exit(0)
    try:
        # test that `date` is a valid date
        datetime.strptime(p_date, "%Y-%m-%d")
    except ValueError:
        print("Please enter a valid date.")
        sys.exit(0)


def validate_tiebreak_episode(p_is_tiebreak_episode: int):
    match p_is_tiebreak_episode:
        case 1:
            p_is_tiebreak_episode = True
        case 2:
            p_is_tiebreak_episode = False
        case _:
            print("Enter a valid number (1 or 2).")
            sys.exit(0)


def validate_youtube_link(p_link: str):
    link_pattern = r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=|playlist\?list=|channel/|c/)?[a-zA-Z0-9_-]+(&[a-zA-Z0-9_=-]*)*$"
    if re.match(link_pattern, p_link):
        pass
    else:
        print("Please enter a valid youtube link.")
        sys.exit(0)


def validate_num_races(p_num_races: int):
    if p_num_races > 0:
        pass
    else:
        print("Please enter an integer more than 0.")
        sys.exit(0)


def validate_num_item_or_dodge(p_num_item_or_dodge: int):
    if p_num_item_or_dodge > 0:
        pass
    else:
        print("Please enter an integer of 0 or more.")
