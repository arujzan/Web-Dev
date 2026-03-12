N = int(input())
a = list(map(int, input().split()))
count = 0
i = 1

while i < N:
    if(a[i] > a[i - 1]):
        count += 1
    i += 1

print(count)