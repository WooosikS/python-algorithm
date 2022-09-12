n = int(input())
llist = list(map(int, input().split()))

cnt = 0
res = 0

for i in range(n):
    if llist[i] == 1:
        res += 1
        cnt += res
    else:
        res = 0

print(cnt)
