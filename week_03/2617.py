import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split())
graphB = [[] for _ in range(N+1)]
graphS = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graphB[a].append(b)
    graphS[b].append(a)
def dfs(graph, vertex):
    visit[vertex] = True
    for next_vertex in graph[vertex]:
        if not visit[next_vertex]:
            dfs(graph, next_vertex)
count = 0
for i in range(1, N + 1):
    visit = [False] * (N + 1)
    dfs(graphB, i)
    if sum(visit) - 1 >= N // 2 + 1:
        count += 1
    else:
        visit = [False] * (N + 1)
        dfs(graphS, i)
        if sum(visit) - 1 >= N // 2 + 1:
            count += 1
print(count)