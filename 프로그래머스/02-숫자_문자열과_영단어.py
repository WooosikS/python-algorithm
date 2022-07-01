#  https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dic = [ "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    for index, value in enumerate(dic):
        if value in s:
            s = s.replace(value, str(index))
    return int(s)        # int로 변환해줘야 통과



s1 = "one4seveneight"
print(solution(s1))
s2 = "23four5six7"
print(solution(s2))
s3 = "2three45sixseven"
print(solution(s3))
s4 = "123"
print(solution(s4))
