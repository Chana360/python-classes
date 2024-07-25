user= ('ola', 4, 'atilola', 32, 4.7, 'olayinka', 20, 18, 32)
print("The elements in the tuple are: ", user)

print("\n")

print("The number of occurrences for each elements are: ")
print("olayinka occurrence is: ", user.count('olayinka'))
print("32 occurrence is: ", user.count(32))
print("4.7 occurrence is: ", user.count(4.7))
print("4 occurrence is: ", user.count(4))
print("20 occurrence is: ", user.count(20))
print("18 occurrence is: ", user.count(18))

print("\n")

print("... and the index for the element occurring twice are: ")
print("olayinka take the index: ", user.index('olayinka'))
print("32 take the index: ", user.index(32))