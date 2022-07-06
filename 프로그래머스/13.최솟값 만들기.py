#  https://school.programmers.co.kr/learn/courses/30/lessons/12941


def solution(A,B):

    A.sort()
    B.sort(reverse=True)
    answer = 0

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

arr1 = [1, 4, 2]
arr2 = [5, 4, 4]
print(solution(arr1, arr2))