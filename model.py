# FILE: /registration_and_login_project/model.py

# Installing for database interaction: #8:
# pip install sqlalchemy
# pip install pymysql

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Defining the database connection parameters: #9:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
DATABASE = 'registration_and_login'
PORT = '3306'

# Creating database through terminal (mariadb/mysql): #10:
# CREATE DATABASE registration_and_login;

# Creating the connection to the database: #11:
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Creating the SQLAlchemy engine and session: #12:
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Defining the class model for the database table: #13:
Base = declarative_base()

# Creating tables in the database if they don't exist: #14:
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(30))
    password = Column(String(500))

# Creating tables based on defined models: #15:
Base.metadata.create_all(engine)

# Consult the database: #16:
# USE registration_and_login;
# SHOW TABLES;

# Edson Copque | https://linktr.ee/edsoncopque