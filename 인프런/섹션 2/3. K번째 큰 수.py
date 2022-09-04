import sys

n, k = map(int, sys.stdin.readline().split())
llist = list(map(int, sys.stdin.readline().split()))
set_llist = set()      # set은 중복을 제거하는 자료구조

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            set_llist.add(llist[i]+llist[j]+llist[m])       # set 자료구조는 appand가 아니라 add로 써야한다.

set_llist = list(set_llist)     # set 자료구조는 sort 개념이 없다. 그래서 다시 list화
set_llist.sort(reverse=True)
print(set_llist[k-1])



# my solution

# n, m = map(int, input().split())
# llist = list(map(int, input().split()))
# sum_llist = []

# for i in range(0, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             sum_llist.append(llist[i] + llist[j] + llist[k])

# sum_llist = set(sum_llist)
# sum_llist = list(sum_llist)
# sum_llist.sort()
# print(sum_llist[-m])