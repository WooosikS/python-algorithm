import sys

n = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))
max = -2147000000
res = 0 

def digit_sum(x):
    sum = 0
    while x > 0:
        sum = sum + x%10
        
    

for x in llist:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)