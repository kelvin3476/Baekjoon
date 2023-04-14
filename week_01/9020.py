def Goldbach():
    check = [True] * 10000
    # m = int(10000 ** 0.5)
    
    for i in range(2, 101):               #<=== #for i in range(2, m+1)
        if check[i] == True:
            for j in range(2*i, 10000, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        A = n // 2
        B = A

        for _ in range(10000):
            if check[A] and check[B]:
                print(A, B)
                break
            A -= 1
            B += 1

Goldbach()

# def gold():
#     num= [True] * 10000
#     m = int(10000 ** 0.5)

#     for i in range(2, m+1):
#         if num[i] == True:
#             for j in range(2*i, 10000, i):
#                 num[j] = False

#     T= int(input())
#     for _ in range(T):
#         N= int(input())

#         a= N // 2
#         b= a

#         for _ in range(2, 10000):
#             if num[a] and num[b]:
#                 print(a,b)
#                 break

#             a -= 1
#             b += 1
        
# gold()