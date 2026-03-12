N = int(input())
a = [int(x) for x in input().split()]
count = 0

i = 1
while i < N - 1:
    if(a[i] > a[i - 1] and a[i] > a[i + 1]):
        count += 1
    i += 1

print(count)