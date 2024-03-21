#!/usr/bin/python3
"""
display state objects from the mysql database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine object that will interact with the mysql
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                          argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    s_state = session.query(State).filter(State.name.like('%a%'))\
                                  .order_by(State.id).all()
    for state in s_state:
        print("{}: {}".format(state.id, state.name))
    session.close()
