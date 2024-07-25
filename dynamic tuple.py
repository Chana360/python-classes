values = ()
item_no = int(input("How many item did you buy? ").strip())

for i in range(item_no):
    items = int(input("Enter a value: "))
    value_list = list(values)
    value_list.append(items)
    values = tuple(value_list)
print(values)

total = 0
for i in values:
    total = total + i
print(total)