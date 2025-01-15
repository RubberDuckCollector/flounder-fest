"""
To be used for creating the tables in the database
"""

import sqlite3
import inspect
import mymodules.sql_statements

def first_boot(database: str):  # msg is an optional but recommended argument
    # get the current call stack
    stack = inspect.stack()

    # the frame at index 1 is the caller's frame
    caller_frame = stack[1]

    # get file name from the caller's frame
    caller_file = caller_frame.filename

    try:
        with sqlite3.connect(database) as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

            cursor = conn.cursor()  # this is like saying `f = open(filename, "r")`, cursor is like f
            try:
                for _, value in mymodules.sql_statements.init_table_statements.items():
                    cursor.execute(value)
                    conn.commit()
            except sqlite3.OperationalError as e:
                print("Failed to create tables:", e)
            print(f"Successfully created tables (if they didn't exist already). This procedure was called from file: {caller_file}")

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)
