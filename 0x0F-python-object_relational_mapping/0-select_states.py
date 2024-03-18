#!/usr/bin/python3
"""List state."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            password=argv[2], db=argv[3], charset="utf-8")
    curr = con.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    con.close()
