#!/usr/bin/python3

from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    if (len(argv) == 4):
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                               argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        query = session.query(State, City).filter(State.id == City.state_id).all()
        for State, City in query:
            print(f'{City.name}: ({City.id}) {City.name}')
        session.close()
