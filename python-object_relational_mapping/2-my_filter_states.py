#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
where the state name matches the user input
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database,
                         charset="utf8")
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name='{}'\
          ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
