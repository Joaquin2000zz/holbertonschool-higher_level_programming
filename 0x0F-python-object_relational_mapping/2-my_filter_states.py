#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa using MYSQLdb
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) > 3):
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=argv[1],
                             passwd=argv[2],
                             db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states \
WHERE name LIKE '{}'".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
