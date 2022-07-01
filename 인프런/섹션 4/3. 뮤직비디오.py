import sys

def Count(capacity):
    cnt = 1
    sum = 0

    for i in llist:
        if sum + i > capacity:
            cnt += 1
            sum = i
        else:
            sum += i
    return cnt

n, m = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))

maxx = max(llist)       #  노래들 중에서 가장 큰 노래(분)

lt = llist[0]
rt = sum(llist)
res = 0

while lt <= rt :
    mid = ( lt + rt ) // 2

    if mid >= maxx and Count(mid) <= m:     # 노래중에서 가장 긴 노래보다는 dvd 하나의 용량이 크거나 같아야 한다.
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)