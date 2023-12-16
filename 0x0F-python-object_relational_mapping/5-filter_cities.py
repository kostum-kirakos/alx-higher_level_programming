#!/usr/bin/python3
"""  lists all cities from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )

    curr = conn.cursor()
    query = """SELECT cities.name
               FROM cities
               INNER JOIN states
               ON states.id=cities.state_id WHERE states.name = %s"""
    param = (sys.argv[4],)
    curr.execute(query, param)
    result = curr.fetchall()
    tolist = list(r[0] for r in result)
    res = ', '.join(tolist)
    print(res)
    curr.close()
    conn.close()
