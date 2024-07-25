# infinite loop
num = 1
while num <= 10:
    print(num)

# # this loop keeps on running as far as the condition is true
num = 0
while num <= 10:
    print(num)
    num = num + 1
# #
# # this loop also keeps on running as far as the condition is true, but arrangement does matter!
# # here increment comes before the print and at 10, it fulfils the condition and then still print
num = 0
while num <= 10:
    num = num + 1
    print(num)
