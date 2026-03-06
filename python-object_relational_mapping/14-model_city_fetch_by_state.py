#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_14_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    user, password, db_name = sys.argv[1:4]
    engine = create_engine(f"mysql+mysqldb://{user}:{password}@localhost/{db_name}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
