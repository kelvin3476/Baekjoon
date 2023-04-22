# source code: https://great-park.tistory.com/m/21
# reference: https://veggie-garden.tistory.com/28

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 
N, M = map(int, input().split()) # 6, 5
# 인접 리스트 -> 인덱스를 그대로 정점의 번호를 사용
graph = list([] for _ in range(N+1))

# 연결 요소 개수
cnt = 0

for _ in range(M): # (5)
    a, b = map(int, input().split()) # (1, 2) (2, 5) (5, 1) (3, 4) (4, 6)
    graph[a].append(b) # graph[[],[2],[],[4],[6],[2,1],[]]
    graph[b].append(a) # graph[[],[2,5],[1,5],[4],[3,6],[2,1],[4]]

# DFS
visited = [False] * (N+1) # [False, False, False, False, False, False, False]
def DFS(x):
    visited[x] = True # i = 1: [False, True, True, False, False, True, False] => i = 3: [False, True, True, True, True, True, True]

    for node in graph[x]:
        if not visited[node]:
            DFS(node)

cnt = 0

for i in range(1, N+1): #(1, 7)
    if not visited[i]:
        DFS(i)
        cnt += 1 # when True => cnt += 1

print(cnt) # 2