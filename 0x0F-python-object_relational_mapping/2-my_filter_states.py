#!/usr/bin/python3
"""List state."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    query = """
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"""
    query = query.format(argv[4])
    cur.execute(states)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
