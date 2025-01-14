import sqlite3
import readline
import sql_statements


def user_written_statements(conn):
    # start loop of user inputs
    user_input = input("Write SQL statement\n> ")

    cur = conn.cursor()
    cur.execute(user_input)
    conn.commit
    return cur.lastrowid


def main():

    database = "flounderfest.db"
    
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
