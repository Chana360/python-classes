user = ('ola', 4, 'ola', 6, 7, 5, 4)
print("The tuple created is: ", user)

user_list = list(user)

user_list.remove(4)
user_list.remove('ola')

print("\n")

print("After removing re-occurring elements: ")
user_tuple = tuple(user_list)
print(user_tuple)
