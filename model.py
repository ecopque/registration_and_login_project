# FILE: /registration_and_login_project/model.py

# pip install sqlalchemy #8:
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Defining a database connection (previously): #9:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
DATABASE = 'registration_and_login'
PORT = '3306'

# Creating database through terminal (mariadb/mysql): #10:
# CREATE DATABASE registration_and_login;

CONN = f'mysql+pymysql//'




# Edson Copque | https://linktr.ee/edsoncopque