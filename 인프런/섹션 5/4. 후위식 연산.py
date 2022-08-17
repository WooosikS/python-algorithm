import sys

strr = sys.stdin.readline().rstrip()
stack = []

for x in strr:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2+n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)

print(stack[0])