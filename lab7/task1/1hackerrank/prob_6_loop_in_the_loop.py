N, M = map(int, input().split())

for i in range(N // 2):
    pattern_count = 2 * i + 1
    row = (".|." * pattern_count).center(M, "-")
    print(row)

print("WELCOME".center(M, "-"))


for i in reversed(range(N // 2)):
    pattern_count = 2 * i + 1
    row = (".|." * pattern_count).center(M, "-")
    print(row)