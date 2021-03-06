#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa using MYSQLdb
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) > 3):
        try:
            db = MySQLdb.connect(host='localhost', user=argv[1],
                                 passwd=argv[2], db=argv[3])
            cur = db.cursor()
            # Print results in comma delimited format
            cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
ORDER BY states.id, states.name ASC;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
            cur.close()
            db.close()
        except Exception:
            pass
