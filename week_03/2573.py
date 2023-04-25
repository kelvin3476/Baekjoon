import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def dfs(x, y):
    for direction in range(4):
        nx = dx[direction]+x
        ny = dy[direction]+y
        if 0 <= nx < N and 0 <= ny < M and visited[nx][ny]:
            visited[nx][ny] = False
            if iceMap[nx][ny] != 0:
                dfs(nx, ny)
N, M = map(int, input().split())
iceMap = []
for _ in range(N):
    iceMap.append(list(map(int, input().split()))[:M])
year = 0
visited = [[False]*M for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
    year += 1
    # 빙산 녹는 처리
    for i in range(N):
        for j in range(M):
            if iceMap[i][j] != 0:
                visited[i][j] = True
                state = iceMap[i][j]
                for k in range(4):
                    nx = dx[k]+i
                    ny = dy[k]+j
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                        if iceMap[nx][ny] == 0:
                            state -= 1
                            if state == 0:
                                break
                iceMap[i][j] = state
    # 빙산 영역 체크
    field = 0
    for i in range(N):
        for j in range(M):
            if iceMap[i][j] != 0 and visited[i][j]:
                dfs(i, j)
                field += 1
            elif iceMap[i][j] == 0 and visited[i][j]:
                visited[i][j] = False
    if field >= 2:
        print(year)
        break
    elif field == 0:
        print(0)
        break