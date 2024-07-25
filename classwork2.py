num1 = int(input('enter the number: '))
num2 = int(input('enter the second number: '))
todo = int(input('enter 1. to add. 2. to subtract. 3. to multiply and 4. to divide: '))

if todo == 1:
    sum1 = num1 + num2
    print(sum1)
elif todo == 2:
    sub = num1 - num2
    print(sub)
elif todo == 3:
    mult = num1 * num2
    print(mult)
elif todo == 4:
    div = num1 / num2
    print(div)
else:
    print('invalid')
