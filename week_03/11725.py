# source code: https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-11725-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-DFS

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node): # (1)
    visited[node] = 1 # visited[1] = 1
    for i in graph[node]: # i = 0: graph[1]
        if not visited[i]:
            parent[i] = node # parent[2] = 4, 
            dfs(i)

N = int(input()) # 7

graph = [[] for _ in range(N+1)] # [[], [], [], [], [], [], [], []]
visited = [0] * (N+1) # [0, 1, 1, 1, 1, 1, 1, 1]
parent = [0] * (N+1) # [0, 0, 4, 6, 1, 3, 1, 4]

while True:
    try:
        a, b = map(int, input().split()) # (1,6) (6,3) (3,5) (4,1) (2,4) (4,7)
        graph[a].append(b)
        graph[b].append(a) # [[], [6,4], [4], [6,5], [1,2,7], [3], [1,3], [4]]
    except:
        break

# 방문처리를 해주기 때문에 꼭 필요하진 않음.
# for i in range(N+1): # (8)
#     graph[i].sort() # [[], [4,6], [4], [5,6], [1,2,7], [3], [1,3], [4]]

dfs(1)

print(*parent[2:], sep='\n')