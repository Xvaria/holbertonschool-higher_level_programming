#!/usr/bin/python3
'''lists all states with a name starting with N (upper N)\
   from the database hbtn_0e_0_usa'''
from sys import argv
import MySQLdb

if __name__ == '__main__':
    con = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = con.cursor()
    cursor.execute("SELECT states.id, states.name FROM states WHERE\
                    ASCII(states.name) = 78 ORDER BY states.id")
    for item in cursor:
        print(item)
