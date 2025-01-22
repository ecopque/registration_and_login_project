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
    def check_data(cls, ck_name, ck_email,  ck_password):
        if len(ck_name) > 50 or len(ck_name) < 3:
            return 2
        if len(ck_email) > 30:
            return 3
        if len(ck_password) > 500 or len(ck_password) < 6:
            return 4
        else:
            return 1

    @classmethod
    def register(cls, rg_name, rg_email, rg_password):
        session = return_session()
        
        user = session.query(Person).filter(Person.email == rg_email).all()
        if len(user) > 0:
            return 5
        
        verified_data = cls.check_data(rg_name, rg_email, rg_password)
        if verified_data != 1:
            return verified_data # Data is not valid.
        
        try:
            # Generating password hash:
            password_hash = hashlib.sha256(rg_password.encode()).hexdigest()

            # Creating the Person object and inserting it into the database:
            new_user = Person(name=rg_name, email=rg_email, password=password_hash)
            session.add(new_user)
            session.commit()
            return 1
                                
        except Exception as error:
            print(f'Error: {error}')
            return 3

# print(RegisterController.register('Edson', 'me@ecop.org', '123456'))



# Edson Copque | https://linktr.ee/edsoncopque