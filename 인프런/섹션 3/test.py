import sys

llist = [ list(map(int, sys.stdin.readline().split())) for _ in range(7) ]

cnt = 0

for i in range(3):
    for j in range(7):
        tmp = llist[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if llist[i+k][j] != llist[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)