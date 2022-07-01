import sys

n = int(sys.stdin.readline())
body = []

for _ in range(n):
    h, w = map(int ,sys.stdin.readline().split())
    body.append((h, w))
body.sort(reverse=True)
largest = 0
cnt = 0


for x, y in body:
    if y > largest:
        cnt += 1
        largest = y

print(cnt)