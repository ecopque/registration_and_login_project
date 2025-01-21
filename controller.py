# FILE: /registration_and_login_project/controller.py

# Imports: #17:
from model import Person
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

# Defining a function to return a new SQLAlchemy session: #18:
def return_session():
    USER = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    DATABASE = 'registration_and_login'
    PORT = '3306'

    # Creating the connection to the database: #19:
    CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    # Creating the SQLAlchemy engine and session: #20:
    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class RegisterController():
    @classmethod
    def check_data(cls, name, email,  password):
        if len(name) > 50 or len(name) < 3:
            return 2

# Edson Copque | https://linktr.ee/edsoncopque