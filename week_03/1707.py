# CHAT GPT
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, group): # (1,0) (3,1) (2,0) ()
    visited[node] = True # visited[1] = True, visited[3] = True, visited[2] = True
    groups[node] = group # groups[1] = 0, groups[3] = 1, groups[2] = 0

    for next_node in graph[node]: # 3 in graph[1], 1 in graph[3], 2 in graph[3]
        if not visited[next_node]: # not visited[3]
            if not dfs(next_node, 1 - group): # not dfs(3, 1)
                return False
        elif groups[next_node] == group:
            return False
        
    return True

T = int(input()) # 2

for _ in range(T): # (2)
    V, E = map(int, input().split()) # (3,2) and (4,4)
    graph = [[] for _ in range(V+1)] # [[],[],[],[]] and [[],[],[],[],[]]
    visited = [False] * (V+1) # [False, True, True, True] and [False, False, False, False, False]
    groups = [-1] * (V+1) # [-1, 0, 0, 1] and [-1, -1, -1, -1, -1]

    for _ in range(E): # (2) and (4)
        a, b = map(int, input().split()) # E = 2: (1,3) (2,3), E = 4: (1,2) (2,3) (3,4) (4,2)
        graph[a].append(b)
        graph[b].append(a) # [[],[3],[3],[1,2]] and [[],[2],[1,3,4],[2,4],[3,2]]

    is_bipartite = True
    for i in range(1, V + 1): # (1, 4) and (1, 5)
        if not visited[i]:
            if not dfs(i, 0):
                is_bipartite = False
                break

    if is_bipartite:
        print("YES")
    else:
        print("NO")
