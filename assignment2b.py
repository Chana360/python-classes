user = input('What is your name? ')
print('Hello,' f'{user}')

password = input('Enter password: ')
password1 = input('Confirm password: ')

count = 1

while password != password1 and count <=3:
    password1 = input('Enter password again: ')
    count += 1
print('Maximum number of times is exceeded!')
if password == password1:
    print('Login successful')
