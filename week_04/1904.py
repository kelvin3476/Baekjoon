# 상향식 풀이법 (Bottom-Up)

import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * 1000001
dp[1] = 1
dp[2] = 2

def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746

tile(n)
print(dp[n])

# 하향식 풀이법 (파이썬 에선 안됌 X, but C++ 가능)