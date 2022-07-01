# https://www.acmicpc.net/problem/21278

import sys

n, m = map(int, sys.stdin.readline().split())

INF = 2147000000

visited = [ [INF] * (n+1) for _ in range(n+1) ]

for _ in range(m):
    a, b = map(int ,sys.stdin.readline().split())
    visited[a][b] = 1
    visited[b][a] = 1

for a in range(1, n+1):
    for b in range(1, b+1):
        if a == b:
            visited[a][b] = 0

for k in range(1, n + 1):
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            visited[a][b] = min(visited[a][b], visited[a][k] + visited[k][b])

min_sum = INF
result = list()
for i in range(1, n):  # 건물 2개를 뽑는다.
    for j in range(2, n + 1):
        sum_ = 0
        for k in range(1, n + 1):  # 모든 집을 방문하면서 거리를 측정
            sum_ += min(visited[k][i], visited[k][j]) * 2  # k -> i, k -> j 중에 짧은 거리 합치기
        if sum_ < min_sum:
            min_sum = sum_
            result = [i, j, sum_]

print(*result)