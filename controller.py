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

# Register Controller: Class for handling user registration: #21:
class RegisterController():
    # Function to validate the input data for registration: #22:
    @classmethod
    def check_data(cls, ck_name, ck_email,  ck_password):
        if len(ck_name) > 50 or len(ck_name) < 3:
            # return 2
            return '[Name] length is invalid. It should be between 3 and 50 characters.'
        if len(ck_email) > 30:
            # return 3
            return '[Email] length is invalid. It should be up to 30 characters.'
        if len(ck_password) > 500 or len(ck_password) < 6:
            # return 4
            return '[Password] length is invalid. It should be between 6 and 500 characters.'
        else:
            # return 1
            return 'Data is valid.'

    # Function to handle the registrations process: #23:
    @classmethod
    def register(cls, rg_name, rg_email, rg_password):
        session = return_session()
        
        # Check if the e-mail is already taken: #24:
        user = session.query(Person).filter(Person.email == rg_email).all()
        if len(user) > 0:
            # return 5
            return 'The email already exists.'
        
        verified_data = cls.check_data(rg_name, rg_email, rg_password)
        if verified_data != 'Data is valid.':
            return verified_data # Data validation error message.
        
        try:
            # Generating password hash: #25:
            password_hash = hashlib.sha256(rg_password.encode()).hexdigest()

            # Creating the Person object and inserting it into the database: #26:
            new_user = Person(name=rg_name, email=rg_email, password=password_hash)
            session.add(new_user)
            session.commit()
            # return 1
            return 'Registration completed successfully.'
                                
        except Exception as error:
            # return 6
            return f'An internal error occurred: {str(error)}'

# Login Controller: Class for handling user login: #27:
class LoginController():
    # Function to handle the login process: #28:
    @classmethod
    def login(cls, lg_email, lg_password):
        session = return_session()
        lg_password = hashlib.sha256(lg_password.encode()).hexdigest()
        
        # Query the database to check for matching e-mail and password: #29:
        logged = session.query(Person).filter(Person.email == lg_email).filter(Person.password == lg_password).all()

        # Check if the login was successfully: #30:
        if len(logged) > 0:
            return {'logged': True, 'id': logged[0].id}
        else:
            # return False
            return 'Invalid email or password.'
        
class RemoveController():
    @classmethod
    def remove(cls, rm_email):
        session = return_session()
        user_to_remove = session.query(Person).filter(Person.email == rm_email).first()

        if not user_to_remove:
            return 'User with the given e-mail does not exist.'
        
        try:
            session.delete(user_to_remove)
            session.commit()
            return 'User removed successfully.'
        
        except Exception as error:
            print(f'Error removing the user: {str(error)}')


# Testing user registration:
# print(RegisterController.register('Edson', 'me@ecop.org', '123456'))

# Testing user login:
# print(LoginController.login('me@ecop.org', '123456'))

# Edson Copque | https://linktr.ee/edsoncopque