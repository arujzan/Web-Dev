def double_power(a, n):
    return a ** n

a, n = map(float, input().split())
n = int(n)
print(double_power(a, n))