#!/usr/bin/python3
"""
ORM query which shows all the rows containing the a letter in the State.name
"""
from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if (len(argv) == 4):
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(argv[1],
                                       argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        query = session.query(State).filter(State.name.like('%a%'))
        for item in query:
            print(f'{item.id}: {item.name}')
        session.close()
