n = int(input())
e_llist = []

for i in range(n):
    llist = list(map(int, input().split()))
    if llist[0] == llist[1] == llist[2]:
        e_llist.append(10000 + 1000 * llist[0])
    elif (llist[0] == llist[1]) != llist[2]:
        e_llist.append(1000 + llist[0] * 100)
    elif (llist[1] == llist[2]) != llist[0]:
        e_llist.append(1000 + llist[1] * 100)
    elif (llist[0] == llist[2]) != llist[1]:
        e_llist.append(1000 + llist[2] * 100)
    else:
        e_llist.append(max(llist[0], llist[1], llist[2]) * 100)

print(max(e_llist))