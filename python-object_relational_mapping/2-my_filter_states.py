#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where the name matches the argument provided.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=db_name,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to select states matching the provided name
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for state in results:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
