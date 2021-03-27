#!/usr/bin/python3
'''Filter states by user input'''
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
                    states.name = '{}' ORDER BY states.id".format(argv[4]))
    for item in cursor:
        print(item)
