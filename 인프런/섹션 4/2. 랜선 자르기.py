import sys

def Count(len):
    cnt = 0

    for i in llist:
        cnt += (i//len)
    return cnt

k, n = map(int, sys.stdin.readline().split())
llist = []
res = 0
largest = 0

for i in range(k):
    tmp = int(sys.stdin.readline())
    llist.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest

while lt <= rt:
    mid = ( lt + rt ) // 2

    if Count(mid) >= n:
        lt = mid + 1
        res = mid
    else:
        rt = mid - 1

print(res)