# https://school.programmers.co.kr/learn/courses/30/lessons/12936
# 프로그래머스 질문하기 글 읽어보기 (설명)

from math import factorial

def solution(n, k):
    answer = []
    llist = list(range(1, n+1))

    while n != 0:
        fact = factorial(n-1)
        answer.append(llist.pop((k-1)//fact))
        n -= 1
        k %= fact
    return answer

n = 3
k = 5

print(solution(n, k))