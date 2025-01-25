# FILE: /registration_and_login_project/testing.py

# pip install sqlalchemy


#####################################################
# model.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Informar dados de conexão:
USER = 'root'
PASSWORD = '123456'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'registration_and_login'

# Variável de conexão:
CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

# Criando engine e session:
engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Criando a base da tabela:
Base = declarative_base()

# Defindo tabela [se não existir]:
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(500))

# Executando tabela:
Base.metadata.create_all(engine)

#####################################################
# controller.py (Registro, Login, Remove)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import hashlib

# Definindo sessão/retorno/conexão:
def return_session():
    USER = 'root'
    PASSWORD = '123456'
    HOST = 'localhost'
    DATABASE = 'registration_and_login'
    PORT = '3306'

    # Definindo variável de conexão:
    CONN = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

    # Definindo engine e session:
    engine = create_engine(CONN, echo=True)
    Session = session(bind=engine)
    return Session()

class RegisterController():
    @classmethod
    def check_data(cls, ck_name, ck_email, ck_password):
        if len(ck_name) > 50 or len(ck_name) < 3:
            return 'aaa'
        
        if len(ck_email) > 30:
            return 'bbb'

        if len(ck_password) > 500 or len(ck_password) < 6:
            return 'ccc'
        
        else:
            return 'Data is valid.'

    @classmethod
    def register(cls, rg_name, rg_email, rg_password):
        session = return_session()

        user_check = session.query(Person).filter(Person.email == rg_email).all()
        if len(user_check) > 0:
            return 'E-mail já existe.'
        
        valid_data = cls.check_data(rg_name, rg_email, rg_password)
        if valid_data != 'Data is valid.':
            return valid_data

        try:
            password_hash = hashlib.sha256(rg_password.encode()).hexdigest()
            new_user = Person(name=rg_name, email=rg_email, password=password_hash)
            session.add(new_user)
            session.commit()
            return 'Usuário registrado com sucesso.'

        except Exception as error:
            print(f'Error:{error}')


class LoginController():
    @classmethod
    def login(cls, lg_email, lg_password):
        session = return_session()

        lg_password = hashlib.sha256(lg_password.encode()).hexdigest()
        logged_check = session.query(Person).filter(Person.email == lg_email).filter(Person.password == lg_password).first()

        if len(logged_check) > 0:
            return f'Login efetuado. {logged_check[0].id}'

        else:
            return 'E-mail ou senha errados.'