x = input()
number = 0
a = len(x) - 1

for i in range(0, len(x)):
    number = number + int(x[i]) * (2 ** a)
    a -= 1

print(number)