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
    curr.execute("""SELECT cities.id, cities.name, states.name
                    FROM cities
                    INNER JOIN states
                    ON states.id=cities.state_id ORDER BY cities.id""")
    result = curr.fetchall()
    for r in result:
        print(r)
    curr.close()
    conn.close()
