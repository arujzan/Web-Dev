N = int(input())
a = list(map(int, input().split()))

i = 0
while i < N - 1:
    if(a[i] * a[i + 1] > 0):
        print("YES")
        break
    i += 1

else: 
    print("NO")