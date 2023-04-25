import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # 5
M = int(input()) # 8
graph = [[] for _ in range(N + 1)] # [[], [], [], [], [], []]
distance = [INF] * (N + 1) # [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]
        
for i in range(M): # (8)
    A, B, C = map(int, input().split()) # (1, 2, 2) (1, 3, 3) (1, 4, 1) (1, 5, 10) (2, 4, 2) (3, 4, 1) (3, 5, 1) (4, 5, 3)
    graph[A].append((B, C)) # [[], [(2,2),(3,3),(4,1),(5,10)], [(4,2)], [(4,1),(5,1)], [(5,3)], []]

start, end = map(int, input().split()) # 1, 5

def dijkstra(start): # (1)
    q = [(0, start)] # q = [(0, 1)]
    distance[start] = 0 # distance[1] = 0 => [1000000000, 0, 1000000000, 1000000000, 1000000000, 1000000000]

    while q: 
        dist, now = heappop(q) # (0, 1) (1, 4) (2, 2) (3, 3) (4, 5) (10, 5)
        if distance[now] < dist: # distance[1] < 0
            continue
        for V, W in graph[now]: # (2,2) in graph[1]
            cost = dist + W # cost = 0 + 2
            if cost < distance[V]: # 2 < distance[2]
                distance[V] = cost # distance[2] = 2
                heappush(q, (cost, V)) # (q, (2, 2))

dijkstra(start)

print(distance[end]) # distance의 마지막 인덱스 값 출력 => [1000000000, 0, 2, 3, 1, 4]