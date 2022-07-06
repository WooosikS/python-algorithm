#  https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = list(map(int, s.split(' ')))
    return str(min(answer)) + " " + str(max(answer))


s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
s3 = "-1 -1"

print(solution(s1))