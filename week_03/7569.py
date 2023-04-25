from collections import deque

m, n, h = map(int, input().split()) # 입력 받기
box = [] # 토마토 상자 정보
for i in range(h):
    box.append([list(map(int, input().split())) for j in range(n)])

# 상하좌우, 앞뒤 방향 설정
dh = [-1, 1, 0, 0, 0, 0] # 앞뒤 방향
dn = [0, 0, -1, 1, 0, 0] # 상하 방향
dm = [0, 0, 0, 0, -1, 1] # 좌우 방향

# BFS 함수 정의
def bfs():
    # 초기 익은 토마토 위치 큐에 추가
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    q.append((i, j, k, 0))

    # BFS 수행
    while q:
        # 큐에서 하나의 토마토 정보를 꺼냄
        th, tn, tm, days = q.popleft()
        # 상하좌우, 앞뒤 방향으로 탐색
        for i in range(6):
            nh = th + dh[i]
            nn = tn + dn[i]
            nm = tm + dm[i]
            # 상자의 범위를 벗어나지 않으면서,
            # 익지 않은 토마토 라면
            if 0 <= nh < h and 0 <= nn < n and 0 <= nm < m and box[nh][nn][nm] == 0:
                # 토마토 익힘
                box[nh][nn][nm] = 1
                # 새로 익은 토마토 정보 큐에 추가
                q.append((nh, nn, nm, days + 1))
    # 모든 토마토가 익었는지 확인
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return -1
    # 최소 일수 반환
    return days

# BFS 수행
result = bfs()

# 결과 출력
print(result)
