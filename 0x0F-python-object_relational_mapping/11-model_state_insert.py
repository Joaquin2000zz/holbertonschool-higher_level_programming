#!/usr/bin/python3
"""
inserts a new state using ORM
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

        new_state = State(name='Louisiana')

        session.add(new_state)
        session.commit()

        query = session.query(State).filter_by(name="Louisiana").all()
        if (query is not None):
            for item in query:
                print(item.id)
        else:
            print("Not found")
        session.close()
