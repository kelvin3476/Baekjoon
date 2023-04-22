# source code: https://codable.tistory.com/8

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input()) # 5

A = input().rstrip() # 10111

graph = [[] for _ in range(n+1)] # [[],[],[],[],[],[]]
place = [0] * (n+1) # [0,1,0,1,1,1]
visited = [0] * (n+1) # [0,0,1,0,0,0]

for i in range(len(A)): # (5)
    if A[i] == '1':
        place[i+1] = 1

for _ in range(n-1):
    a, b = map(int, input().split()) # (1, 2) (2, 3) (2, 4) (4, 5)
    graph[a].append(b)
    graph[b].append(a) # [[],[2],[1,3,4],[2],[2,5],[4]]
    
def dfs(node):
    res = 0 
    for next_node in graph[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0
for i in range(1, n+1): # (1, 6)
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1)
    else:
        for next_node in graph[i]:
            if place[next_node] == 1:
                ans += 1
print(ans)