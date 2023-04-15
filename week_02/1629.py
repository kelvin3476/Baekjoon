import sys
input = sys.stdin.readline

A, B, C = map(int, input().split()) # 10 11 12 

def multiplication(A, B, C):
    if B == 1:
        return A % C 
    elif B % 2 == 0:
        return multiplication(A, B//2 ,C) ** 2 % C # (10 ** 5) ** 2 % 12
    else:
        return (multiplication(A, B//2, C) ** 2) * A % C # ((10 ** 5) ** 2) * 10 % 12

print(multiplication(A, B, C))