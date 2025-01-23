# FILE: /registration_and_login_project/view.py

from controller import RegisterController

while True:
    print('===== [MENU] =====')
    user_decision = input('Enter 1 to [register]\n'
                          'Enter 2 to [login]\n'
                          'Enter 3 to [exit]: ')
    
    if user_decision == 1:
        name = input('Enter your [name]: ')
        email = input('Enter your [e-mail]: ')
        password = input('Enter your [password]: ')
        result = RegisterController.register(name, email, password)

        if result == 2:
            print('Name [length] entered is invalid.')
        elif result == 3:
            print('E-mail [length] entered is invalid.')
        elif result == 4:
            print('Password [length] entered is invalid.')
        elif result == 5:
            print('Entered [e-mail] is already exists.')