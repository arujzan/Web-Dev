v = int(input()) #the speed
t = int(input()) #the time

S = v * t # the distance 
x = S // 109 # how many times it made circles
print(S - 109 * x)