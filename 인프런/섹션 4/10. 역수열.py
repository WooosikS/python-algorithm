import sys

n = int(sys.stdin.readline())
llist = list(map(int, sys.stdin.readline().split()))

llist = llist[::-1]

seq = []

for x in llist:
    seq.insert(x, n)
    n -= 1

print(seq)





# import sys

# n = int(sys.stdin.readline())
# llist = list(map(int, sys.stdin.readline().split()))

# seq = [0] * n

# for i in range(n):
#     for j in range(n):
#         if llist[i] == 0 and seq[j] == 0:
#             seq[j] = i + 1
#             break
#         elif seq[j] == 0:
#             llist[i] -= 1

# for x in seq:
#     print(x, end=' ')