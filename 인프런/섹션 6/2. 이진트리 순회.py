# print문이 재귀함수 맨 밑에 있으면 후위, 중간이면 중위, 맨 위면 전위

import sys

def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2)
        DFS(v*2 + 1)
        print(v, end=' ')      

if __name__=="__main__":
    DFS(1)