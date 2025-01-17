import re
import sys
import pprint
import sqlite3
import readline
import argparse
from datetime import datetime
import mymodules.first_boot
import mymodules.sql_statements
import mymodules.automated_data_entry


"""
variables starting with `p_` denote a parameter.
"""


parser = argparse.ArgumentParser(prog="main-db.py",
                                 description="Flounderfest stats",
                                 epilog="Data may be incorrect, but the project is still fun.")


database = "flounderfest.db"


def user_written_statements(conn):
    # start loop of user inputs
    user_input = input("Write SQL statement\n: ")

    cur = conn.cursor()
    cur.execute(user_input)
    conn.commit
    return cur.lastrowid


def main():
    parser.add_argument("--insert_tracks_played", action="store_true", help="Prompts user for data relating to the tracks played in an episode, then generates and executes SQL INSERT statements based on the user input. Using the `sqlite3` command and entering data manually is much slower.")
    parser.add_argument("--insert_episode_wins", action="store_true", help="Prompts user for data relating to the episode and video and who won that episode. Then generates and executes SQL statements based on the user input. Using the `sqlite3` command and entering data manually is much slower.")

    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    mymodules.first_boot.first_boot(database)

    if args.insert_tracks_played:
        mymodules.automated_data_entry.insert_tracks_played(database)

    if args.insert_episode_wins:
        mymodules.automated_data_entry.insert_episode_wins(database)

if __name__ == "__main__":
    main()
