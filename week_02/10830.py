import sys
input = sys.stdin.readline

n, b = map(int, input().split()) # n, b = 2, 5
c = []
for _ in range(n):
    c.append(list(map(int, sys.stdin.readline().split())))

# 행렬 곱하기(A*A) 알고리즘
def mul(a, b): # a, b 라는 배열 생성
    result = [[0 for _ in range(n)] for _ in range(n)] # result = [[0,0], [0,0]]
    for i in range(n): # a 배열의 (가로 = i)
        for j in range(n): # b 배열의 (세로 = j)
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

def cal(b, c):
    if b == 1:
        return c
        # 단순 2제곱일 경우
    elif b == 2:
        return mul(c, c)
    else:
        temp = cal(b // 2, c)
        # b가 짝수일 경우 제곱수를 계속 곱하면 된다.
        # AAAA = ((A^2)^2)
        if b % 2 == 0:
            return mul(temp, temp)
        # b가 홀수일 경우 마지막에 A를 곱해줘야한다.
        # AAAAA = ((A^2)^2)*A
        else:
            return mul(mul(temp, temp), c)

result = cal(b, c)

for row in result:
    for num in row:
        print(num % 1000,end= ' ')
    print()