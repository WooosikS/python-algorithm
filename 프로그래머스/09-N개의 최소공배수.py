def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)


def solution(arr):
    answer = arr[0]
    for i in arr:
        answer = lcm(i, answer)
    return answer


llist = [2, 6, 8, 14]
print(solution(llist))