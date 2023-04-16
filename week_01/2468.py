# https://www.youtube.com/watch?v=7R5RlbjuI8U <= source code

from collections import deque

def bfs(si, sj, h): # start i, start j, h 
    q = deque()

    q.append((si,sj))
    v[si][sj]=1 # visited

    while q:
        ci,cj = q.popleft() # current i, current j
        # 네방향, 범위내, 미방문, 높이 > h
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)): # direction i, direction j
            ni,nj = ci+di, cj+dj # next i, next j
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and arr[ni][nj]>h:
                q.append((ni,nj))
                v[ni][nj]=1

def solve(h): # h높이에 대해 잠기지 않는 영역 개수 리턴
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j]==0 and arr[i][j]>h:
                bfs(i,j,h) 
                cnt += 1
    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for h in range(100): # 높이 0 ~ 99 까지 물 높이 지정
    v = [[0]*N for _ in range(N)]
    ans = max(ans, solve(h))
print(ans)

# 용상이형 코드 (DFS 구현 방식 (feat. 현수형))

# DFS
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)
# N = int(input())
# land = []
# land = [list(map(int,input().split())) for i in range(N)]
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# result = 0
# def dfs(x,y,h):
#     if h >= land[x][y]:
#         check[x][y] = True  # 비온 곳 확인
#         return False
#     check[x][y] = True #안전 구역 확인
#     for i in range(4):
#         nx,ny = x+dx[i] , y+dy[i]
#         if(0<= nx < N and
#            0<= ny < N and
#            not check[nx][ny]):
#             dfs(nx,ny,h)
#     return True
# for k in range(max(map(max, land))): # k 가 높이
#     check = [[False]*N for i in range(N)] # 확인한 장소인지 체크
#     sum = 0
#     for i in range(N):
#         for j in range(N):
#            if not check[i][j] and dfs(i,j,k):
#                sum += 1
#     if result < sum :
#         result = sum
# print(result)