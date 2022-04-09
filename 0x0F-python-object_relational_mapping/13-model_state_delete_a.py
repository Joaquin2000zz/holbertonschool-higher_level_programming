#!/usr/bin/python3

from model_state import Base, State
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy import delete

if __name__ == "__main__":
    if (len(argv) == 4):
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(argv[1],
                                       argv[2], argv[3]), pool_pre_ping=True)
        Base.metadata.create_all(engine)


        Del = delete(State).where(State.name.like('%a%'))
        engine.execute(Del)
