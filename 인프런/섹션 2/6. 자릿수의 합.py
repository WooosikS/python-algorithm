import sys

n = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))
max = -2147000000
res = 0 

def digit_sum(x):
    sum = 0
    while x > 0:
        sum = sum + x%10
        x = x // 10
    return sum

for x in llist:
    total = digit_sum(x)
    if total > max:
        max = total
        res = x
print(res)


# my solution
# n = int(input())
# llist = list(map(int, input().split()))
# res = 0
# result = 0
# max = -2147000000

# def digit_sum(x):
#     sum = 0
#     while x > 0:
#         sum = sum + x%10
#         x = x // 10
#     return sum

# for x in llist:
#     res = digit_sum(x)
#     if res > max:
#         max = res
#         result = x
# print(result)