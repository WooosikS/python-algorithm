import sys

def Count(len):                 # 배치할 수 있는 말의 마릿수
    cnt = 1
    end = llist[0]              # 말이 마지막에 배치된 지점

    for i in range(1, n):
         # 두 번째 말을 배치하려고 하는데, 마지막에 배치한 지점의 말 거리 뺌
        if llist[i] - end >= len:       # len보다 크면 말 배치 가능.
            cnt += 1
            end = llist[i]
    return cnt

n, c = map(int, sys.stdin.readline().split())
llist = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    llist.append(tmp)
llist.sort()


lt = 1
rt = llist[n-1] - 1
res = 0

while lt <= rt :
    mid = ( lt + rt ) // 2      # 가장 가까운 두 말의 거리 == mid

    if Count(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1

print(res)