#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to fetch all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result of the query
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
