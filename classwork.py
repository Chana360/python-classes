print('Welcome to CHANA LIB')
# what the user wants to do
print("Enter: \n"
      "1 Sign up\n"
      "2 to Login")

user_list = []
todo = int(input('Choose: '))

if todo == 1:
    def f_name():
        f_name = input('Enter your first name: ')
        user_list.append(f_name)

    def l_name():
        l_name = input('Enter your first name: ')
        user_list.append(l_name)

    def age():
        age = input('Enter your first name: ')
        user_list.append(age)

    def dob():
        dob = input('Enter your first name: ')
        user_list.append(dob)

else:
    print("Cant process your reply!")


def signup():
    f_name()
    l_name()
    age()
    dob()

signup()


