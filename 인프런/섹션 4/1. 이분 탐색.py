import sys

n, m = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
llist.sort()

lt = 0
rt = n -1

while lt <= rt :
    mid = ( lt + rt ) // 2
    if llist[mid] == m:
        print(mid+1)
        break
    elif llist[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1
