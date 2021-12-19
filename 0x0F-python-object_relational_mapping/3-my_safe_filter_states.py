#!/usr/bin/python3
"""
    This script lists all states from the database hbtn_0e_0_usa
    where name matches an argument and is safe from SQL injection
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=(%s) \
                ORDER BY states.id ASC".format(argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
