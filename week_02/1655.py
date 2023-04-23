#source code: https://velog.io/@uoayop/BOJ-1655-%EA%B0%80%EC%9A%B4%EB%8D%B0%EB%A5%BC-%EB%A7%90%ED%95%B4%EC%9A%94Python
import sys
import heapq
input = sys.stdin.readline

n = int(input()) # 7
max_h = [] # [-1], [-2, -1], [-2, -1, 99], [-5, -2, 99, -1]
min_h = [] # [5], [5, 10], [5, 10, 7]

for i in range(n):
    num = int(input())
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if len(max_h) >= 1 and len(min_h) >= 1 and max_h[0] * -1 > min_h[0]:
        max_value = heapq.heappop(max_h) * -1
        min_value = heapq.heappop(min_h)
        
        heapq.heappush(max_h, min_value * -1)
        heapq.heappush(min_h, max_value)

    print(max_h[0] * -1)

# ex) [1, 5, 2, 10, -99, 7, 5]
# num = 1 👉🏻 left = [-1] / right = []
# num = 5 👉🏻 left = [-1], right = [5]
# num = 2 👉🏻 left = [-2,-1], right = [5]
# num = 10 👉🏻 left = [-2,-1], right = [5,10]
# num = -99 👉🏻 left = [-2,-1,99], right = [5,10]
# num = 7 👉🏻 left = [-2,-1,99], right = [5,7,10]
# num = 5 👉🏻 left = [-5,-2,-1,99], right = [5,7,10]
