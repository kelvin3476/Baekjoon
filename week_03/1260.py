# source code: https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-1260%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visit_list[v] = 1 
    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in range(1, n + 1): # (1, 5)
            if visit_list[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit_list[i] = 1

def dfs(v):
    visit_list2[v] = 1
    print(v, end = " ")
    for i in range(1, n + 1):
        if visit_list2[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, input().split()) # 4, 5, 1

graph = [[0] * (n + 1) for _ in range(n + 1)] # [[0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 0, 0]]
visit_list = [0] * (n + 1) # [0, 1, 1, 1, 1]
visit_list2 = [0] * (n + 1) # [0, 1, 1, 1, 1]

for _ in range(m): # (5)
    a, b = map(int, input().split()) # (1, 2) (1, 3) (1, 4) (2, 4) (3, 4) 
    graph[a][b] = graph[b][a] = 1 

dfs(v)
print()
bfs(v)