# FILE: /registration_and_login_project/view.py

from controller import RegisterController, LoginController

while True:
    print('===== [MENU] =====')
    user_decision = int(input('Enter 1 to [register]\n'
                          'Enter 2 to [login]\n'
                          'Enter 3 to [exit]: '))
    
    if user_decision == 1:
        name = input('Enter your [name]: ')
        email = input('Enter your [e-mail]: ')
        password = input('Enter your [password]: ')
        result_register = RegisterController.register(name, email, password)

        if result_register == 2:
            print('Name [length] entered is invalid.')
        elif result_register == 3:
            print('E-mail [length] entered is invalid.')
        elif result_register == 4:
            print('Password [length] entered is invalid.')
        elif result_register == 5:
            print('Entered [e-mail] is already exists.')
        elif result_register == 6:
            print('Internal error.')
        elif result_register == 1:
            print('Registration completed successfully.')
        
    if user_decision == 2:
        email = input('Enter your [e-mail]: ')
        password = input('Enter your [password]: ')
        result_login = LoginController.login(email, password)

        if not result_login:
            print('Invalid e-mail or password.')
        else:
            print(result_login)
    
    else:
        break