# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    llist = []

    for i in s:
        if len(llist) == 0:
            llist.append(i)
        else:
            if i == llist[-1]:
                llist.pop()
            else:
                llist.append(i)
    if len(llist) == 0:
        return 1
    else:
        return 0

s1 = "baabaa"
print(solution(s1))
s2 = "cdcd"
print(solution(s2))




#  이렇게 풀면 시간초과 남.
# def solution(s):
#     llist = list(s)
#     l_len = len(llist)
#     cnt = 0

#     while cnt < l_len -1:
#         if llist[cnt] == llist[cnt+1]:
#             del llist[cnt]
#             del llist[cnt]
#             if len(llist) == 0:
#                 return 1
#             cnt = 0
#         else:

#             cnt += 1
#     return 0

# s1 = "baabaa"
# print(solution(s1))
# s2 = "cdcd"
# print(solution(s2))