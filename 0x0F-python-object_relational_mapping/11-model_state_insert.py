#!/usr/bin/python3
""" adds the State  to the database  """

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    louisiana = State(name='Louisiana')
    session.add(louisiana)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(new_state.id))
    session.close()
