# FILE: /registration_and_login_project/testing.py

# pip install sqlalchemy


#####################################################
# model.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

USER = 'ROOT'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'registration_and_login'

CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# CREATE DATABASE registration_and_login;

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(500))

Base.metadata.create_all(engine)

# controller:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Person
import hashlib

def return_session():
    USER = 'root'
    USER = 'ROOT'
    PASSWORD = '123456'
    HOST = 'localhost'
    PORT = '3306'
    DATABASE = 'registration_and_login'

    CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    return Session()

class RegisterController():
    @classmethod
    def check_data(cls, ck_name, ck_email, ck_password):
        if len(ck_name) > 50 or len(ck_name) < 3:
            return 'Nome inválido.'
        if len(ck_email) > 100:
            return 'E-mail inválido.'
        if len(ck_password) > 500 or len(ck_password) < 6:
            return 'Password inválido.'
        else:
            return 'Data is valid.'
    
    @classmethod
    def register(cls, rg_name, rg_email, rg_password):
        session = return_session()

        user = session.query(Person).filter(Person.email == rg_email).first()
        if len(user) > 0:
            return 'E-mail já existe.'
        
        valid_data = cls.check_data(rg_name, rg_email, rg_password)
        if valid_data != 'Data is valid.':
            return valid_data

        try:
            hash_password = hashlib.sha256(rg_password.encode()).hexdigest()
            new_user = Person(name=rg_name, email=rg_email, password=hash_password)
            session.add(new_user)
            session.commit()
            return 'Registro realizado com sucesso.'
        
        except Exception as error:
            print(f'Error: {error}')

class LoginController():
    @classmethod
    def login(cls, lg_email, lg_password):
        session = return_session()
        lg_password = hashlib.sha256(lg_password.encode()).hexdigest()

        logged = session.query(Person).filter(Person.email == lg_email).filter(Person.password == lg_password).first()

        if len(logged) > 0:
            return f'Logged: {True}, Id: {logged[0].id}'
        else:
            return 'E-mail ou senha inválidos.'

class RemoveController():
    @classmethod
    def remove(cls, rm_email):
        session = return_session()

        user_email = session.query(Person).filter(Person.email == rm_email)
        if not user_email:
            return 'E-mail não existe.'
        
        try:
            session.delete(user_email)
            session.commit()
            return 'Usuário deletado com sucesso.'
        
        except Exception as error:
            print(f'Error: {error}')

# view:

from controller import RegisterController, LoginController, RemoveController
while True:
    print('===== [MENU] =====')
    user_decision = input(int(('Enter 1 to register\n'
                        'Enter 2 to login\n'
                        'Enter 3 to remove\n'
                        'Enter 4 to exit: ')))

    if user_decision == 1:
        name = input(str('Enter your name: '))
        email = input(str('Enter your e-mail: '))
        password = input('Enter your password: ')

        new_user = RegisterController.register(name, email, password)
        print(new_user)

    if user_decision == 2:
        email = input(str('Enter your e-mail: '))
        password = input(str('Enter your password: '))

        user_login = LoginController.login(email, password)
        
        if not user_login:
            print('Invalid user or password')
        else:
            print(f'Login efetuado: {user_login}.')

    if user_decision == 3:
        email = input('Enter your e-mail: ')
        user_email = RemoveController.remove(email)

        if not user_email:
            print(f'Usuário não existe.')
        else:
            print(f'Usuário removido: {user_email}')
    
    else:
        break