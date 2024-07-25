def login():
    print('Welcome to CHANA LIB')
    # what the user wants to do
    print("Enter: \n"
          "1 Sign up\n"
          "2 to Login")
    todo = int(input('Choose: '))

    if todo == 1:
        def data():
            user_list = []
            f_name = input('Enter your first name: ')
            user_list.append(f_name)
            l_name = input("Enter your last name: ")
            user_list.append(l_name)
            age = int(input("Enter your age: "))
            user_list.append(age)
            dob = input("Enter your date of birth: ")
            user_list.append(dob)
            print("Sign up successful")


    elif todo == 2:
        print("The login page isn't available right now!")

    else:
        print("You must have entered the wrong thing!")

login()




