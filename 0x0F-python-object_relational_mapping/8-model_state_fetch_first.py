#!/usr/bin/python3
"""
module which select the first row of the State table with ORM
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

        query = session.query(State).first()
        if (query is not None):
            print(f'{query.id}: {query.name}')
        else:
            print("Nothing")
