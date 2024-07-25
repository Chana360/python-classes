score = (10, 20, 30, 40, 50)
total = 0

for i in range(len(score)):
    total = total + score[i]
    print(total)

if total >= 200:
    print("Promoted!")
else:
    print("Repeat")