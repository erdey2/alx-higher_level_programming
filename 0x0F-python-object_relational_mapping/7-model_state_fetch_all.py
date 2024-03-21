#!/usr/bin/python3
"""
list all State objects from mysql database using ORM(MySQLalchemy)
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create an engine object that will interact with the mysql
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s_state = session.query(State).order_by(State.id).all()
    for state in s_state:
        print("{}: {}".format(state.id, state.name))
    session.close()
