# source code: https://velog.io/@ssulee0206/%EB%B0%B1%EC%A4%80-2178%EB%B2%88-%EB%AF%B8%EB%A1%9C%ED%83%90%EC%83%89%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque

N, M = map(int, input().split()) # 4, 6

graph = []

for _ in range(N):
    graph.append(list(map(int, input()))) # [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]

def BFS(x, y):
    # 이동할 상, 하, 좌, 우 방향 정의
    dx = [-1,1,0,0] # 북, 남 => 상, 하
    dy = [0,0,-1,1] # 서, 동 => 좌, 우

    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft() # 현재 좌표
        # 현재 위치에서 4가지 방향 위치 확인
        for i in range(4):
            nx = x + dx[i] # 상,하 이동
            ny = y + dy[i] # 좌,우 이동
            # 위치 벗어나면 안되므로 조건 추가 and 벽이므로 진행 불가
            if nx<0 or nx>=N or ny<0 or ny>=M or graph[nx][ny]==0:
                continue
            # 벽이 아니므로 이동 가능
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))

    # 마지막 값에서 카운트 값 뽑기
    return graph[N-1][M-1] # 자리에 도달했을때 값을 반환

print(BFS(0,0)) # 초기 값 설정

# [1,0,1,1,1,1] => [3, 0, 9, 10, 11, 12]
# [1,0,1,0,1,0]	=> [2, 0, 8, 0, 12, 0]
# [1,0,1,0,1,1]	=> [3, 0, 7, 0, 13, 14]
# [1,1,1,0,1,1]	=> [4, 5, 6, 0, 14, 15]