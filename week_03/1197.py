# source code: https://velog.io/@yoopark/baekjoon-1197

import sys
input = lambda: sys.stdin.readline().rstrip()

V, E = map(int, input().split()) # 3, 3 

# kruskal algorithm
edges = [] 
for _ in range(E): # (3)
    A, B, C = map(int, input().split()) # A정점, B정점, 가중치
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2]) # C(cost)가 적은것부터 정렬

    
# union-find
parent = [i for i in range(V+1)] # [0, 1, 2, 3]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x]) # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b: # 작은 쪽이 부모가 된다. (한 집합 관계라서 부모가 따로 있는 건 아님)
        parent[b] = a
    else:
        parent[a] = b        

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in edges:
    # cost 가 적은 edge부터 하나씩 추가해가면서 같은 부모를 공유하지 않을 때(사이클 없을 때)만 확정
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)