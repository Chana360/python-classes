user = input('What is your name? ')
print('Welcome,' f'{user}')
secretnum = 45
guess = int(input('Guess a number: '))

count = 1
while count < 4:
    if guess != secretnum:
        guess = int(input('Try again: '))
        count = count + 1
    if guess == secretnum:
        print('user win')
        break
    if count == 4:
        print("user lose")
        break
