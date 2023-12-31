#!/usr/bin/python3

"""
Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print("{}: ({}) {}".format(instance[0], instance[1], instance[2]))
