#source code:https://velog.io/@yj_lee/%EB%B0%B1%EC%A4%80-18352%EB%B2%88-%ED%8A%B9%EC%A0%95-%EA%B1%B0%EB%A6%AC%EC%9D%98-%EB%8F%84%EC%8B%9C-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split()) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호

graph = [[] for i in range(N+1)] # 그래프 생성

for i in range(M):
    A, B = map(int, input().split()) # A => B 도시로 이동하는 단방향 도로가 존재한다.  (# A, B는 서로 다른 자연수 이다.)
    graph[A].append(B) # [[],[2,3],[3,4],[],[]]

d = [-1] * (N+1) # 노드 간 거리 -1로 초기화 => [-1, -1, -1, -1, -1]
d[X] = 0 # 시작 노드의 거리는 0으로 => [-1, 0, -1, -1, -1]

queue = deque([X]) # 시작 노드 => deque([1])

while queue:
    start = queue.popleft() # 현재 노드 pop start = 1, deque([]) => start = 2,  deque([3]) => start = 3, deque([4]), start = 4, deque([]) 

    for nx in graph[start]: # 현재 갈 수 있는 모든 노드 탐색 2, 3 in [2,3]
        if d[nx] == -1: # 방문한적 없는 노드이면 d[2] == -1
            d[nx] = d[start]+1 # 방문 처리 d[2] = d[1]+1 => [-1, 0, 1, -1, -1] => [-1, 0, 1, 1, -1] => [-1, 0, 1, 1, 2]
            queue.append(nx) # deque([2]) => deque([2, 3]) => deque([3, 4])

city = False # K 거리에 해당하는 도시가 있는지 판별

for i in range(1, N+1):
    if d[i] == K:
        print(i)
        city = True # 도시가 존재

if city == False: # 도시가 존재 안할때
    print(-1)