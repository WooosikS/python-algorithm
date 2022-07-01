import sys

n = int(sys.stdin.readline())
llist = [ list(map(int, sys.stdin.readline().split())) for _ in range(n) ]
llist.insert(0, [0]*n )
llist.append([0]*n)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0

for x in llist:
    x.insert(0, 0)
    x.append(0)

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(llist[i][j] > llist[i+dx[k]][j+dy[k]] for k in range(4) ):
            cnt += 1
print(cnt)