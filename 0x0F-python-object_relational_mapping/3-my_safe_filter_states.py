#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    curr = conn.cursor()
    query = """SELECT * FROM states WHERE name
                 LIKE %s ORDER BY states.id"""
    param = (sys.argv[4] + '%',)
    curr.execute(query, param)
    result = curr.fetchall()
    for row in result:
        print(row)
    curr.close()
    conn.close()
