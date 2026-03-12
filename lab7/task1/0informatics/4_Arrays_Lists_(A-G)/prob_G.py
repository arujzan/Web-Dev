N = int(input())
a = [int(x) for x in input().split()]

i = 0
j = N - 1

while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

print(*a)