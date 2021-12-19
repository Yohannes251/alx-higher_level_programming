#!/usr/bin/python3
"""
    This script lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states \
                 ON state_id=states.id \
                 ORDER BY cities.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
