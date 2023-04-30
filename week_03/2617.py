# Reference: https://velog.io/@johnny/baek-2617

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split()) # 구슬의 개수, 쌍의 개수

graphB = [[] for _ in range(N+1)] # 무게가 더큰 구슬 리스트
graphS = [[] for _ in range(N+1)] # 무게가 더적은 구슬 리스트

for _ in range(M):
    a, b = map(int, input().split()) # 구슬의 쌍
    graphB[a].append(b)
    graphS[b].append(a)

def dfs(graph, vertex):
    visit[vertex] = True
    for next_vertex in graph[vertex]:
        if not visit[next_vertex]:
            dfs(graph, next_vertex)

count = 0 # 무게가 중간이 될수 없는 구슬의 수 초기화

for i in range(1, N + 1):
    visit = [False] * (N + 1) # graphB visited
    dfs(graphB, i)
    if sum(visit) - 1 >= N // 2 + 1:
        count += 1
    else:
        visit = [False] * (N + 1) # graphS visited
        dfs(graphS, i)
        if sum(visit) - 1 >= N // 2 + 1:
            count += 1

print(count)