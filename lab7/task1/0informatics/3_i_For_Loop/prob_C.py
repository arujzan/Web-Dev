x = int(input())
y = int(input())

for i in range(x, y + 1):
    if(i ** 0.5 == int(i ** 0.5)):
        print(i)
