#!/usr/bin/python3
"""Add the State object Louisiana to the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <user> <passwd> <db>")
        sys.exit(1)
    user, password, db_name = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
