import sys
import sqlite3
import mymodules.first_boot
import mymodules.sql_statements
import mymodules.input_validation

def insert_tracks_played(table: str):
    """
    Prompts user for data relating to the tracks played in an episode
    then generates and executes SQL statements based on the user input.
    Using the `sqlite3` command and entering data manually is much slower.
    """

    database = "tracks_played"

    try:
        with sqlite3.connect(database) as conn:  # this is like saying `f = open(filename, "r")`, conn is like f
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

            cursor = conn.cursor()

            # mymodules.first_boot.first_boot("../flounderfest.db")

            start_id = int(input("Enter start id (primary key): "))
            mymodules.input_validation.validate_start_id(start_id)
            cursor.execute("SELECT MAX(id) FROM tracks_played")
            max_id = cursor.fetchone()[0]  # fetchone() returns a tuple, so access the first element
            if max_id is not None:
                if start_id <= max_id:
                    print("""
            You can't create records with the same primary keys. Also to be safe, you
            can't create records with primary keys lower than what has already been
            created (e.g if you make records 1-5, you're not allowed to make record 0 
            through this automated process, since the program doesn't know how many
            tracks - and therefore records - you will add).
            The current highest primary key in {table} is {max_id}, and the next viable primary key is {max_id+1}.""")
                    sys.exit(0)
                else:
                    pass
            else:
                pass

            season = int(input("Enter season: "))
            mymodules.input_validation.validate_season(season)

            episode = int(input("Enter episode: "))
            mymodules.input_validation.validate_episode(episode)

            is_final_episode_of_season = int(input("Final episode of the season? (1 = yes, 2 = no): "))
            is_final_episode_of_season = mymodules.input_validation.validate_final_episode_of_season(is_final_episode_of_season)

            date = input("Enter date (YYYY-MM-DD): ").strip()
            date = f"'{date}'"
            mymodules.input_validation.validate_date(date)

            is_tiebreak_episode = int(input("Is tiebreak episode? (1 = yes, 2 = no): "))
            is_tiebreak_episode = mymodules.input_validation.validate_tiebreak_episode(is_tiebreak_episode)

            twd98_video_title = input("Enter TWD98 video title (inside ''): ").strip()
            twd98_video_title = f"'{twd98_video_title}'"
            mymodules.input_validation.validate_youtube_title(twd98_video_title)

            twd98_video_link = input("Enter TWD98 video link (inside ''): ").strip()
            twd98_video_link = f"'{twd98_video_link}'"
            mymodules.input_validation.validate_youtube_link(twd98_video_link)


            count = 0
            tracks = []  # all the tracks they race in the episode
            track = ""  # user input
            while True:
                track = input(f"Enter track on race {count+1} : ")
                track = f"'{track}'"
                if track == "'-1'":
                    break
                tracks.append(track)  # append the user input to the `tracks[]` list
                count += 1  # a count is kept for the race number on screen
            num_races = len(tracks)
            # pprint.pprint(tracks, indent=4)  # DEBUG

            if num_races < 1:  # presence check for tracks played in that episode
                print("Please enter at least 1 track.")
                sys.exit(0)
            else:
                pass

            print("Num races:", num_races)

            # put together the SQL statements
            statements = []
            for i in range(num_races):
                # in this case it's `tracks_played`
                statements.append(f"INSERT INTO {table}(id, season, episode, is_final_episode_of_season, date, is_tiebreak_episode, twd98_video_title, twd98_video_link, race, track) VALUES ({start_id}, {season}, {episode}, {is_final_episode_of_season}, {date}, {is_tiebreak_episode}, {twd98_video_title}, {twd98_video_link}, {i+1}, {tracks[i]})")
                # increment PRIMARY KEY
                # so the code doesn't try to assign the same primary key to multiple records,
                # which cannot make sense
                start_id += 1  

            # pprint.pprint(statements, indent=4)  # DEBUG

            # execute the statements generated
            try:
                for i in statements:
                    cursor.execute(i)
                    conn.commit()
            except sqlite3.OperationalError as e:
                print("Error inserting data:", e)
            print("Successfully inserted track data.")

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
