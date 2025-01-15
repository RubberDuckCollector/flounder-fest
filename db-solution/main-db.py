import re
import sys
import sqlite3
import readline
import argparse
import sql_statements
import input_validation
from datetime import datetime


"""
variables starting with `p_` denote a parameter.
"""


parser = argparse.ArgumentParser(prog="main-db.py",
                                 description="Flounderfest stats",
                                 epilog="May be incorrect.")


def user_written_statements(conn):
    # start loop of user inputs
    user_input = input("Write SQL statement\n> ")

    cur = conn.cursor()
    cur.execute(user_input)
    conn.commit
    return cur.lastrowid


def main():

    database = "flounderfest.db"

    parser.add_argument("--insert_tracks_played", action="store_true", help="Prompts user for data relating to the tracks played in an episode, then generates and executes SQL INSERT statements based on the user input. Using the `sqlite3` command and entering data manually is much slower.")
    
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()

    try:
        with sqlite3.connect(database) as conn:  # this is like saying `f = open(filename, "r")`, conn is like f
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

            cursor = conn.cursor()
            try:
                for key, value in sql_statements.init_table_statements.items():
                    cursor.execute(value)
                    conn.commit()
            except sqlite3.OperationalError as e:
                print("Failed to create tables:", e)

            """
            Prompts user for data relating to the tracks played in an episode
            then generates and executes SQL statements based on the user input.
            Using the `sqlite3` command and entering data manually is much slower.
            """
            if args.insert_tracks_played:
                start_id = int(input("Enter start id (primary key) > "))
                input_validation.validate_start_id(start_id)

                season = int(input("Enter season > "))
                input_validation.validate_season(season)

                episode = int(input("Enter episode > "))
                input_validation.validate_episode(episode)

                is_final_episode_of_season = int(input("Final episode of the season? (1 = yes, 2 = no) > "))
                input_validation.validate_final_episode_of_season(is_final_episode_of_season)

                date = input("Enter date (YYYY-MM-DD) > ")
                input_validation.validate_date(date)

                is_tiebreak_episode = int(input("Is tiebreak episode? (1 = yes, 2 = no) > "))
                input_validation.validate_tiebreak_episode(is_tiebreak_episode)

                twd98_video_title = input("Enter TWD98 video title > ")

                twd98_video_link = input("Enter TWD98 video link > ")
                input_validation.validate_youtube_link(twd98_video_link)

                nmeade_video_title = input("Enter Nmeade video title > ")

                nmeade_video_link = input("Enter Nmeade video link > ")
                input_validation.validate_youtube_link(nmeade_video_link)

                num_races = int(input("Enter number of races > "))
                input_validation.validate_num_races(num_races)


            # user inputs
            # while True:
            #     try:
            #         user_written_statements(conn)
            #     except sqlite3.Error as e:
            #         print("Error:", e)


    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)


if __name__ == "__main__":
    main()
