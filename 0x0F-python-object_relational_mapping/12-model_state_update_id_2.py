#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    quer = session.query(State).filter(State.id.like(2)).first()
    if quer:
        quer.name = "New Mexico"
    session.commit()
    session.close()
