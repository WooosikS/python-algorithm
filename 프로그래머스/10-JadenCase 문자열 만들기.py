# 문자열의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

def solution(s):
    strr = s.split(' ')
    answer = ''

    for i in range(len(strr)):
        strr[i] = strr[i].capitalize()
    answer = ' '.join(strr)
    return answer

s = "a a a a a a a a"
s1 = "3people unFollowed me"
s2 = "for the last week"

print(solution(s))