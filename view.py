# FILE: /registration_and_login_project/view.py

from controller import RegisterController, LoginController, RemoveController

# Main Loop: User menu for registration or login: #31:
while True:
    print('===== [MENU] =====')
    # Asking the user for their decision: #32:
    user_decision = int(input('Enter 1 to [register]\n'
                          'Enter 2 to [login]\n'
                          'Enter 3 to [remove]\n'
                          'Enter 4 to [exit]: '))
    
    # Registration Flow: If the user chooses to register: #33:
    if user_decision == 1:
        name = input('Enter your [name]: ')
        email = input('Enter your [e-mail]: ')
        password = input('Enter your [password]: ')

        # Calling the RegisterController to register the user: #34:
        result_register = RegisterController.register(name, email, password)
        
        # Handling registration results and providing feedback: #35:
        # if result_register == 2:
        #     print('Name [length] entered is invalid.')
        # elif result_register == 3:
        #     print('E-mail [length] entered is invalid.')
        # elif result_register == 4:
        #     print('Password [length] entered is invalid.')
        # elif result_register == 5:
        #     print('Entered [e-mail] is already exists.')
        # elif result_register == 6:
        #     print('Internal error.')
        # elif result_register == 1:
            # print('Registration completed successfully.')
        print(result_register)
    
    # Login Flow: If the user chooses to login: #36:
    if user_decision == 2:
        email = input('Enter your [e-mail]: ')
        password = input('Enter your [password]: ')

        # Calling the LoginController to login the user: #37:
        result_login = LoginController.login(email, password)

        if not result_login:
            print('Invalid e-mail or password.')
        else:
            print(result_login)

    # Login flow: Removing account:
    if user_decision == 3:
        email = input('Enter the [e-mail] you want to remove: ')

        result_remove = RemoveController.remove(email)

        if not result_remove:
            print('Invalid e-mail.')
        else:
            print(result_remove)
    
    # Exit Condition: If the user chooses to exit the program: #38:
    else:
        break

# Edson Copque | https://linktr.ee/edsoncopque