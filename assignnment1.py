user_list = []

# welcome
while True:
    print('Welcome to CHANA LIB')
    # what the user wants to do
    print("Enter: \n"
          "1 Sign up\n"
          "2 to Login")
    todo = int(input('Choose: '))

    if todo == 1:
        message = input('Enter a secret message here: ')
        user_list.append(message)

        f_name = input('Enter your first name: ')
        user_list.append(f_name)

        l_name = input("Enter your last name: ")
        user_list.append(l_name)

        age = int(input("Enter your age: "))
        user_list.append(age)

        dob = input("Enter your date of birth: ")
        user_list.append(dob)

        username = input("Enter a username: ")
        user_list.append(username)

        password = input("Enter your password: ")
        user_list.append(password)

        con_password = input("Please confirm password: ")
        while password != con_password:
            con_password = input("Please confirm your password: ")
        print("Sign up successful")
        print(user_list[1:])

    elif todo == 2:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        while password != user_list[6]:
            password = input("PLease confirm password: ")
        print("Login successful!")
        print(user_list[0])
        break

    else:
        print("You must have entered the wrong thing!")
