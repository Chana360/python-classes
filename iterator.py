set_of_names = {'ola', 'garce', 'atilola'}

iterator = iter(set_of_names)
single = next(iterator)

if single == 'ola':
    print("Yes")
else:
    print("No")
