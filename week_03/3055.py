# source code: https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-3055-%ED%83%88%EC%B6%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python

from collections import deque

r, c = map(int, input().split()) # 3, 3
graph = [list(input()) for _ in range(r)] # [['D', '.', '*'], ['.', '.', '.'], ['.', 'S', '.']]
visited = [[-1] * c for _ in range(r)] # [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]


def bfs():
    q = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*": # 물의 위치
                q.appendleft((i, j)) # *** 물의 위치가 여러개 일 경우 q에 모두 추가 해줘야함 ***
                visited[i][j] = 0 # 물 방문 처리
            elif graph[i][j] == "S": # 고슴도치의 위치
                q.append((i, j))
                visited[i][j] = 0 # 고슴도치 방문처리

    while q:
        x, y = q.popleft()

        for i in range(4): # 방향 이동
            nx, ny = x + dx[i], y + dy[i] # 물, 고슴도치 이동했을때 위치

            if not 0 <= nx < r or not 0 <= ny < c: # 범위 밖에 안벗어난 경우
                continue
            if visited[nx][ny] != -1: # 이동하는 다음 위치에 방문 안했을경우
                continue
            if graph[nx][ny] == "*" or graph[nx][ny] == "X": # 이동한 다음 위치가 물이 차있거나 돌 인경우 // 예외 처리
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "*": # 이동한 다음 위치가 비버의 굴이고 물이 차있는 경우 // 예외 처리
                continue
            if graph[nx][ny] == "D" and graph[x][y] == "S": # 이동한 다음 위치가 비버의 굴이고 고슴도치의 위치인 경우 // 결과값 구하기
                return visited[x][y] + 1 # 비버의 굴을 도착했으니 + 1 해주고 방문처리 완료 및 성공

            q.append((nx, ny)) # 이동한 위치 q에 저장
            visited[nx][ny] = visited[x][y] + 1 # 거리 1씩 증가
            graph[nx][ny] = graph[x][y] # 이동한 위치로 변경 

    return "KAKTUS" # 안전하게 비버의 굴로 이동 불가능

result = bfs() # 최소 거리 결과 저장

print(result) # 결과값 출력