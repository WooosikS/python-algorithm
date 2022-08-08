import sys

num, m = map(int, sys.stdin.readline().split())
num = list(map(int, str(num)))
stack = [] 

for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m]
res = ''.join(map(str, stack))

print(res)


# ex1)
# input :     5276823 3
# output :    7823

# ex2)
# input :     9977252641 5
# output :    99776