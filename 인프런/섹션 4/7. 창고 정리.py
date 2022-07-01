import sys

n = int(sys.stdin.readline())
width = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
width.sort()

for _ in range(m):
    width[-1] = width[-1] -1
    width[0] = width[0] + 1
    width.sort()

print(width[-1] - width[0])