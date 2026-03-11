x = input()
reversed = str()

for digit in x:
    reversed = digit + reversed

res = int(reversed)
print(res)