import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split()) # 3, 15
coins = []
for i in range(n): # (3)
    coins.append(int(sys.stdin.readline())) # [1, 5, 12]

visited = [False] * 1000001
q = deque()
q.append((0, 0))

while q: 
    cnt, cur = q.popleft()
    if cur == k: # 가능한 경우
        print(cnt) # 최소 개수 출력
        break
    for coin in coins:
        if cur + coin <= k and not visited[cur + coin]:
            visited[cur + coin] = True # 방문처리
            q.append((cnt+1, cur+coin)) 

if cur != k: # 불가능한 경우 -1 출력 // ** 예외 처리
    print(-1)