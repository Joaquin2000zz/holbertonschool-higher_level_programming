#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa using MYSQLdb
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    if (len(argv) > 3):
        db = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3])
        cur = db.cursor()
        # Print results in comma delimited format
        cmd = "SELECT cities.name FROM cities INNER JOIN states ON \
cities.state_id = states.id WHERE states.name LIKE BINARY %s"
        cur.execute(cmd, (argv[4], ))
        rows = cur.fetchall()
        if (rows is not None):
            Len = len(rows)
            for i in range(Len):
                print(rows[i][0], end='')
                if (i == Len - 1):
                    print()
                else:
                    print(", ", end='')
            cur.close()
            db.close()
