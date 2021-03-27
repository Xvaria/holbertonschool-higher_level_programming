#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    enter = sessionmaker()(bind=engine)
    query = enter.query(State).first()
    if query:
        print("{}: {}".format(query.id, query.name))
    else:
        print('Nothing')
