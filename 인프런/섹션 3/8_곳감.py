import sys

n = int(sys.stdin.readline())

llist = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]

m = int(sys.stdin.readline())

for i in range(m):
    h, t, k = map(int, sys.stdin.readline().split())
    if t == 0:
        for _ in range(k):
            llist[h-1].append(llist[h-1].pop(0))
    else:
        for _ in range(k):
            llist[h-1].insert(0, llist[h-1].pop())

s = 0
e = n-1
cnt = 0
for i in range(n):
    for j in range(s, e+1):
        cnt += llist[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(cnt)