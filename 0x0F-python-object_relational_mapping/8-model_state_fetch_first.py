#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """


import MySQLdb
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://" +
                           "{}:{}@localhost/{}".format(sys.argv[1],
                                                       sys.argv[2],
                                                       sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    tus = session.query(State).first()
    if tus is not None:
        print("{}: {}".format(tus.id, tus.name))
    else:
        print("Nothing")
    session.close()