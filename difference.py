set_of_name1 = {'ola', 'grace', 'atilola'}

# #first
set_of_name2 = set()
diff = set_of_name1.difference(set_of_name2)
print(diff)

# #second
set_of_name2 = set()
set_of_name2.update(['grace'])
diff = set_of_name1.difference(set_of_name2)
print(diff)

# #third
set_of_name2 = set()
set_of_name2 = set_of_name1.copy()
diff = set_of_name1.difference(set_of_name2)
print(diff)


