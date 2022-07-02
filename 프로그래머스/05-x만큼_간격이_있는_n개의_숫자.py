# https://programmers.co.kr/learn/courses/30/lessons/12950
# level 1



def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)

    return answer



# x, n = map(int, input().strip().split())
# print(solution(x, n))