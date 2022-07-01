import sys

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    N, s, e, k = map(int ,sys.stdin.readline().split())
    llist  = list(map(int ,sys.stdin.readline().split()))
    llist = llist[s-1:e]
    llist.sort(reverse=False)
    print("#%d %d" %(t+1, llist[k-1]))