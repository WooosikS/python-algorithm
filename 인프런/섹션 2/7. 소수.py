n = int(input())

def isprime(n):
    llist = [ True ] * ( n + 1 )
    m = int(n ** 0.5)

    for i in range(2, m+1):
        if llist[i] == True:
            for j in range(i+i, n+1, i):
                llist[j] = False
    return [ i for i in range(2, n+1) if llist[i] == True]

print(len(isprime(n)))


# n = int(input())

# def isprime(n):
#     llist = [0] * (n + 1)

#     for i in range(2, n+1):
#         if llist[i] == 0:
#             for j in range(i, n+1, i):
#                 llist[j] = 1
#     return [ i for i in range(2, n+1) if llist[i] == 0]

# print(isprime(n))