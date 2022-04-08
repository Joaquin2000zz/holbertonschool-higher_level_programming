#!/usr/bin/python3

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if (len(argv) == 5):
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                               argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        query = session.query(State).filter_by(id='1').all()
        if (len(query) > 0):
            for item in query:
                print(f'{item.id}: {item.name}')
        else:
            print("Nothing")
