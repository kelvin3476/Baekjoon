# 상향식 풀이법 (Bottom-Up) 

# import sys

# input = sys.stdin.readline

# T = int(input()) # 테스트 케이스 개수

# for _ in range(T):
#     N = int(input()) # 동전의 종류 수
#     coins = list(map(int, input().split())) # 동전 가치
#     M = int(input()) # 만들어야 하는 금액

#     dp = [0] * (M+1)
#     dp[0] = 1  # 0원을 만들 수 있는 경우의 수는 1개 (아무 동전도 사용하지 않는 경우)

#     for coin in coins: 
#         for i in range(coin, M+1):
#             dp[i] += dp[i-coin]

#     print(dp[M])

# 하향식 풀이법 (Top-Down)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def count_ways(coins, target, memo):
    if target == 0:
        return 1
    if target < 0:
        return 0
    if len(coins) == 0:
        return 0
    
    key = (len(coins), target)
    if key in memo:
        return memo[key]
    
    memo[key] = count_ways(coins[:-1], target, memo) + count_ways(coins, target-coins[-1], memo)
    return memo[key]

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    N = int(input()) # 동전의 종류 수
    coins = list(map(int, input().split())) # 동전 가치
    M = int(input()) # 만들어야 하는 금액

    memo = {}
    result = count_ways(coins, M, memo)
    print(result)


