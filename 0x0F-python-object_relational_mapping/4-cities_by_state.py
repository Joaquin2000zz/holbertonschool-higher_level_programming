#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa using MYSQLdb
"""
import MySQLdb
from sys import argv

if (len(argv) > 3):
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    # Print results in comma delimited format
    cmd = "SELECT cities.id AS id, cities.name AS Cities, states.name AS Sta\
tes from cities INNER JOIN states ON cities.state_id = states.id"
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
