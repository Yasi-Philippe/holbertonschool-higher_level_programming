#!/usr/bin/python3
"""Change the name of the State with id = 2 to New Mexico"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <user> <passwd> <db>")
        sys.exit(1)
    user, password, db_name = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()
    session.close()
