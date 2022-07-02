# https://programmers.co.kr/learn/courses/30/lessons/12948
# level 1

def solution(phone_number):

    llist = list(phone_number)

    for i in range(len(phone_number)-4):
        llist[i] = '*'

    return ''.join(llist)

phone_number = "01033334444"
print(solution(phone_number))