# https://programmers.co.kr/learn/courses/30/lessons/12950
# level 1



def solution(arr1, arr2):
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

