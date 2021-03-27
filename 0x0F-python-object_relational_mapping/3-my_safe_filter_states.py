#!/usr/bin/python3
'''takes in arguments and displays all values in the states table of\
   hbtn_0e_0_usa where name matches the argument. But this time, write\
   one that is safe from MySQL injections!'''
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
    cursor.execute("SELECT states.id, states.name FROM states\
                    WHERE states.name = %s ORDER BY states.id", (argv[4], ))
    for item in cursor:
        print(item)
