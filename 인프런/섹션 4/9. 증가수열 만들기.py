import sys

n = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))

lt = 0
rt = n - 1
last = 0
tmp = []
res = ""

while lt <= rt :
    if llist[lt] > last :
        tmp.append((llist[lt], "L"))
    if llist[rt] > last:
        tmp.append((llist[rt], 'R'))
    tmp.sort()

    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()

print(len(res))
print(res)