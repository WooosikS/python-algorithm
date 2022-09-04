import sys, math

n = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))
avg = math.ceil(sum(llist)/n)

min = 2147000000

for index, value in enumerate(llist):
    temp = abs(value - avg)
    if temp < min:
        min = temp
        score = value
        res = index+1
    elif temp == min:
        if value > score:
            score = value
            res = index + 1
print(avg, res)