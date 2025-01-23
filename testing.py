# FILE: /registration_and_login_project/testing.py

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Estabelecendo conexão:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'registration_and_login'

# Criando banco de dados no terminal:
# CREATE DATABASE registration_and_login;

# Criando variável de conexão:
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Criando engine e session:
engine = create_engine(CONN, echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# Criando base da tabela:
Base = declarative_base()

# Definindo tabela:
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(500))

# Excecutando tabela:
Base.metadata.create_all(engine)

##################################

