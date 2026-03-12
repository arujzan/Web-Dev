N = int(input())
a = [int(x) for x in input().split()]

i = 0
while i < N:
    if(a[i] % 2 == 0):
        print(a[i])
    i += 1 
    