"""Hackbright Project Tracker.
A front-end for a database that allows users to work with students, class
projects, and the grades students receive in class projects.
"""

import sqlite3

db_connection = sqlite3.connect("hackbright.db", check_same_thread=False)
db_cursor = db_connection.cursor()


def function_name(input):
    """Query in a database."""

    QUERY = """
        SELECT *
        FROM Table
        WHERE input = ?
        """
    db_cursor.execute(QUERY, (input,))
    row = db_cursor.fetchone()
    return row[0], row][1]

if __name__ == "__main__":
    handle_input()
    
    db_connection.close()