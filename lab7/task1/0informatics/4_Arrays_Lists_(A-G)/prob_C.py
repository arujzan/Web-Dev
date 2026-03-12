N = int(input())
a = [int(x) for x in input().split()]
count = 0

i = 0
while i < N:
    if(a[i] > 0):
        count += 1
    i += 1

print(count)