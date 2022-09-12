n = int(input())
llist = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

def isPrime(y):
    if y == 1:
        return False
        
    for j in range(2, y):
        if y % j == 0:
            return False
    else:
        return True

for i in llist:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=' ')