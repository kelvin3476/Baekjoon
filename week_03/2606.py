# CHAT GPT

import sys
input = sys.stdin.readline
n = int(input())  # 컴퓨터의 수: 7
m = int(input())  # 연결된 쌍의 수: 6

graph = [[] for _ in range(n + 1)] # [[], [], [], [], [], [], [], []]
visited = [False] * (n + 1) # [False, False, False, False, False, False, False, False]
count = 0

# 그래프 생성
for _ in range(m): # (6)
    a, b = map(int, input().split()) # (1,2) (2,3) (1,5) (5,2) (5,6) (4,7)
    graph[a].append(b) # [[], [2, 5], [3], [], [7], [2,6], [], []]
    graph[b].append(a) # [[], [2,5], [1,3,5], [2], [7], [1,2,6], [5], [4]]

# DFS 함수 정의
def dfs(v): # (1)
    global count
    visited[v] = True # i = 1: [False, True, True, True, False, True, True, False] => 
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)  # 1번 컴퓨터부터 시작
print(count - 1)  # 1번 컴퓨터는 감염되었으므로 빼준다 4
