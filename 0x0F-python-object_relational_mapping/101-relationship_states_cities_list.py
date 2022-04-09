#!/usr/bin/python3
"""
ORM query to show states with their corresponding cities using relationship
"""
from relationship_state import Base, State
from relationship_city import City
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

        query = session.query(State).order_by(State.id).all()
        for State in query:
            print(f'{State.id}: {State.name}')
            for City in State.cities:
                print(f'    {City.id}: {City.name}')
        session.close()
        session.commit()
        session.close()
