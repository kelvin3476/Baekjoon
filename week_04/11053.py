# 상향식 풀이법 (Bottom-Up)
# import sys

# input = sys.stdin.readline

# n = int(input()) # 6
# a = list(map(int, input().split())) # [10, 20, 10, 30, 20, 50]

# dp = [1] * n # [1, 1, 1, 1, 1, 1] => [1, 2, 1, 3, 2, 4]

# for i in range(n): 
#     for j in range(i):  
#         if a[j] < a[i]: # i=1, j=0
#             dp[i] = max(dp[i], dp[j] + 1)

# print(max(dp))

# 하향식 풀이법 (Top-Down)
import sys

input = sys.stdin.readline

n = int(input()) # 6
a = list(map(int, input().split())) # [10, 20, 10, 30, 20, 50]

dp = [-1] * n # [-1, -1, -1, -1, -1, -1] => [1, 2, 1, 3, 2, 4] 

def lis(index):
    if dp[index] != -1:
        return dp[index]
    
    dp[index] = 1
    for i in range(index-1, -1, -1):
        if a[i] < a[index]:
            dp[index] = max(dp[index], lis(i) + 1)

    return dp[index]

ans = 0
for i in range(n):
    ans = max(ans, lis(i)) # (4)

print(ans)