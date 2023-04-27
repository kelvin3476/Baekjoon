# source code: https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-2748%EB%B2%88-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-2-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# # 상향식 풀이법 (Bottom-Up) 

# import sys
# input = sys.stdin.readline

# n = int(input())
# dp = []
# dp.append(0)
# dp.append(1)

# for i in range(2, n+1):
#     dp.append(dp[i-1]+dp[i-2])
# print(dp[n])

# 하향식 풀이법 (Top-Down) 

import sys
input = sys.stdin.readline

dp = [-1] * 100
dp[0] = 0
dp[1] = 1

def fibo(n):
    if dp[n] == -1:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]

n = int(input())
print(fibo(n))