#!/usr/bin/python3
"""
    This script lists all cities of a state given as argument
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                 JOIN states \
                 ON state_id=states.id \
                 WHERE states.name=(%s) \
                 ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    cities = ""
    for row in rows:
        for col in row:
            cities += col + ", "
    print(cities[:-2])
    cur.close()
    db.close()
