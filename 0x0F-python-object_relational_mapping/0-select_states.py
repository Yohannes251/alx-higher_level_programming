#!/usr/bin/python3
"""
    This script lists all states from the database hbtn_0e_0_usa
"""


from sys import argv
import MySQLdb


db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id")
for row in cur.fetchall():
    print(row)
