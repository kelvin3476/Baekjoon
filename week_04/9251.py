# 상향식 풀이법 (Bottom-Up) 

# import sys

# input = sys.stdin.readline
    
# x = input().strip()
# y = input().strip()

# def LCS(x, y):
#     m = len(x)
#     n = len(y)

#     # dp 배열 초기화
#     dp = [[0] * (n+1) for _ in range(m+1)]
    
#     # LCS 계산
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if x[i-1] == y[j-1]: # 문자가 같은 경우
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#     return dp[m][n]

# print(LCS(x, y))

# [[0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 1, 1, 1, 1, 1], 
#  [0, 1, 1, 1, 2, 2, 2], 
#  [0, 1, 2, 2, 2, 3, 3], 
#  [0, 1, 2, 2, 2, 3, 3], 
#  [0, 1, 2, 2, 2, 3, 4], 
#  [0, 1, 2, 3, 3, 3, 4]]

# 하향식 풀이법 (Top-Down)

import sys
sys.setrecursionlimit(10**4) # recursion error 뜨면 안에 값을 바꿔 볼것
input = sys.stdin.readline
            
x = input().strip()
y = input().strip()

# 재귀함수로 구현한 LCS 함수
def LCS(x, y, m, n, dp):
    if m == 0 or n == 0: # 더 이상 비교항 문자열이 없는 경우
        return 0

    if dp[m][n] != -1: # 이미 계산된 경우
        return dp[m][n]

    if x[m-1] == y[n-1]: # 문자가 같은 경우 
        dp[m][n] = LCS(x, y, m-1, n-1, dp) + 1
    else:
        dp[m][n] = max(LCS(x, y, m-1, n, dp), LCS(x, y, m, n-1, dp))

    return dp[m][n]

# LCS 함수 호출
dp = [[-1] * (len(y)+1) for _ in range(len(x)+1)]
print(LCS(x, y, len(x), len(y), dp))    