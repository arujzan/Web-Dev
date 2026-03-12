'''Solution without using fucntion:

a = [int(x) for x in input().split()]
i = 1
l = len(a)

minimum = a[0]

while i < len(a):
    if a[i] < minimum:
        minimum = a[i]
    i += 1

print(minimum) 
'''

def minimum(a, b ,c ,d):
    nums = [a, b , c, d]
    i = 1
    min = nums[0]

    while i < len(nums):
        if nums[i] < min:
            min = nums[i]
        i += 1
    
    return min

a = [int(x) for x in input().split()]
print(minimum(a[0], a[1], a[2], a[3]))


