# 상향식 풀이법 (Bottom-Up)

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split()) # 물건의 개수와 배낭의 최대 무게 입력 받기

# w, v = [], [] # 물건의 무게와 가치를 저장할 리스트 생성
# for i in range(n):
#     weight, value = map(int, input().split())
#     w.append(weight)
#     v.append(value)

# dp = [[0] * (k+1) for _ in range(n+1)] # dp 테이블 생성
    

# for i in range(1, n+1):
#     for j in range(1, k+1):
#         if j < w[i-1]: # i번째 물건을 선택할 수 없는 경우
#             dp[i][j] = dp[i-1][j]
#         else: # i번쨰 물건을 선택할 수 있는 경우
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i-1]] + v[i-1])

# print(dp[n][k]) # 배낭에 담을 수 있는 최대 가치 출력

# 하향식 풀이법 (Top-Down)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w, v = [], []
for i in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

dp = [[-1] * (k+1) for _ in range(n+1)]

def Bag(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    if i == 0 or j == 0:
        dp[i][j] = 0
        return dp[i][j]
    if j < w[i-1]:
        dp[i][j] = Bag(i-1, j)
        return dp[i][j]
    dp[i][j] = max(Bag(i-1, j), Bag(i-1, j-w[i-1]) + v[i-1])
    return dp[i][j]

print(Bag(n, k))