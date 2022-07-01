# import sys
# from collections import deque

# n, m = map(int, sys.stdin.readline().split())
# weight = list(map(int, sys.stdin.readline().split()))
# weight.sort()

# cnt = 0
# weight = deque(weight)

# while weight:

#     if len(weight) == 1 :
#         cnt += 1
#         break
    
#     if weight[-1] + weight[0] > m:
#         cnt += 1
#         weight.pop()
#     else:
#         cnt += 1
#         weight.popleft()
#         weight.pop()

# print(cnt)

n, m = map(int, input().split())
weight = list(map(int, input().split()))
weight.sort()

cnt = 0
lt = 1
rt = n - 1

while ( lt <= rt ):

    if weight[lt] + weight[rt] > m:
        cnt += 1
        rt -= 1
    else:
        cnt += 1
        lt += 1
        rt -= 1
print(cnt)