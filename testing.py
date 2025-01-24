# FILE: /registration_and_login_project/testing.py

# pip install sqlalchemy


################################################# MODEL:
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Inserindo dados da conexão:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'registration_and_login'

# Criar o banco de dados:
# CREATE DATABASE registration_and_login;

# Criar variável de conexão:
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Variáveis de engine e session:
engine = create_engine(CONN, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# Criando base da tabela:
Base = declarative_base()

# Modelo das tabelas:
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(500))

# Criando tabelas:
Base.metadata.create_all(engine)

# No terminal:
# SHOW DATABASES;
# USE registration_and_login;
# SHOW TABLES;

################################################# CONTROLLER:
