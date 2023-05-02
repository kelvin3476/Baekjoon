# 상향식 풀이법(Bottom-Up)
# import sys
# input = sys.stdin.readline

# def sol():
#     n, m = map(int, input().split())
#     dp = [[float('inf')] * (int((2*n)**0.5)+2) for _ in range(n+1)]
#     dp[1][0] = 0
#     stn = []
#     for _ in range(m):
#         stn.append(int(input()))

#     for i in range(2, n+1):
#         if i in stn:
#             continue
#         for v in range(1, int((2*i)**0.5) + 1):
#             dp[i][v] = min(dp[i-v][v-1], dp[i-v][v], dp[i-v][v+1]) + 1
    
#     result = min(dp[n])
#     if result == float('inf'):
#         print(-1)
#     else:
#         print(result)

# sol()

# 하향식 풀이법(Top-Down)
import sys

inf = 2000000000
n, m = map(int, input().split())
cache = [[-1] * 200 for _ in range(10000)]
chk = [False] * 10000

for i in range(m):
    stone = int(input())
    chk[stone - 1] = True

def dp(now, x):
    if now >= n - 1:
        return 0 if now == n - 1 else inf
    if chk[now]:
        return inf
    ret = cache[now][x]
    if ret != -1:
        return ret
    ret = dp(now + x + 1, x + 1) + 1
    if now != 0:
        ret = min(ret, 1 + dp(now + x, x))
    if x >= 2:
        ret = min(ret, 1 + dp(now + x - 1, x - 1))
    cache[now][x] = ret
    return ret

result = dp(0, 0)
if result >= inf:
    result = -1

print(result)
