# source code: https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-2665%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Dijkstra

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
room = []
for _ in range(N):
    room.append(list(map(int, input().rstrip())))
visited = [[0] * N for _ in range(N)]

def dijkstra():
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, [0, 0, 0])
    visited[0][0] = 1
    while heap:
        a, x, y = heappop(heap)
        if x == N - 1 and y == N - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if room[nx][ny] == 0:
                    heappush(heap, [a + 1, nx, ny])
                else:
                    heappush(heap, [a, nx, ny])

dijkstra()