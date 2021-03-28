#!/usr/bin/python3
'''lists all State objects from the database hbtn_0e_6_usa'''
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    enter = sessionmaker()(bind=engine)
    nstate = State(name="Louisiana")
    enter.add(nstate)
    enter.commit()
    query = enter.query(State).filter_by(name='Louisiana').first()
    print("{}".format(query.id))
