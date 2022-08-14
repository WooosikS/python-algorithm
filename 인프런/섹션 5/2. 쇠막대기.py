import sys

strr = sys.stdin.readline().rstrip()
stack = []
sum = 0

for i in range(len(strr)):
    if strr[i] == '(':
        stack.append(strr[i])
    else:
        stack.pop()
        if strr[i-1] == '(':
            sum += len(stack)
        else:
            sum += 1
print(sum)