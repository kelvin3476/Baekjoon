import sys

input = sys.stdin.readline

N, M = map(int, input().split()) # 2, 4
graph = [[] for _ in range(N+1)] # [[], [], [], [], []]
indegree = [0] * (N+1) # [0, 0, 0, 0, 0]
    
# 그래프와 진입차수 초기화    
for i in range(M): #(2)
    A, B = map(int, input().strip().split()) # 4, 2
    graph[A].append(B) # [[], [], [], [1], [2]]
    indegree[B] += 1 # [0, 1, 1, 0, 0]

# 위상정렬 
def Topological_sort(graph, indegree):
    result = [] # [4, 2, 3, 1]
    stack = [] # [3, 4]

    # 진입차수가 0인 정점을 스택에 추가.
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            stack.append(i)

    # 스택이 빌 때까지 반복.
    while stack:
        node = stack.pop() # node = 4, node = 2, node = 3, node = 1
        result.append(node)

        # 해당 정점에서 출발하는 모든 간선을 제거.
        for v in graph[node]: # v = 2 in graph[4] v = 1 in graph[3]
            indegree[v] -= 1 # indegree[2] -= 1 => [0, 1, 0, 0, 0], indegree[1] -= 1 => [0, 0, 0, 0, 0]

            # 진입차수가 0인 정점을 스택에 추가
            if indegree[v] == 0: # indegree[2] == 0
                stack.append(v) # [3, 2], [1]

    return result

# 위상 정렬 수행
result = Topological_sort(graph, indegree) # [4, 2, 3, 1]

# 결과 출력
if len(result) == N:
    print(*result)
else:
    print('해당 그래프는 DAG가 아닙니다.')