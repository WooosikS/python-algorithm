import sys

n, k = map(int ,sys.stdin.readline().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)


# my solution

# import sys

# n, k = map(int, sys.stdin.readline().split())

# llist = []

# for i in range(1, n+1):
#     if n % i == 0:
#         llist.append(i)
#     else:
#         pass

# if len(llist) < k:
#     print(-1)
# else:
#     print(llist[k-1])