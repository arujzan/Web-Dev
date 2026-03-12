N = int(input())

while N % 2 == 0:
    N //= 2

while N == 1:
    print("YES")
    break

while N != 1:
    print("NO")
    break