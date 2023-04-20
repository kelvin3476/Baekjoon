# Chat GPT 
from collections import deque

# 보드의 크기 입력 받기
n = int(input())

# 보드 초기화
board = [[0] * (n+1) for _ in range(n+1)]

# 사과의 위치 입력 받기
k = int(input())
for _ in range(k):
    row, col = map(int, input().split())
    board[row][col] = 1

# 뱀의 방향 변환 정보 입력 받기
l = int(input())
turns = []
for _ in range(l):
    time, direction = input().split()
    turns.append((int(time), direction))

# 초기 뱀 위치 및 방향 설정
snake = deque([(1,1)])
direction = 1 # 1:동, 2:남, 3:서, 4:북

# 뱀 이동 함수
def move():
    global direction
    
    # 뱀 머리 위치
    row, col = snake[-1]
    
    # 뱀 이동
    if direction == 1: # 동쪽으로 이동
        col += 1
    elif direction == 2: # 남쪽으로 이동
        row += 1
    elif direction == 3: # 서쪽으로 이동
        col -= 1
    else: # 북쪽으로 이동
        row -= 1
    
    # 벽에 부딪히면 게임 종료
    if row < 1 or row > n or col < 1 or col > n:
        return False
    
    # 뱀이 자기 몸통에 부딪히면 게임 종료
    if (row, col) in snake:
        return False
    
    # 뱀 이동 및 길이 유지
    snake.append((row, col))
    if board[row][col] == 1: # 사과 먹은 경우
        board[row][col] = 0
    else: # 사과 못 먹은 경우
        snake.popleft()
    
    return True

# 게임 시작
time = 0
turn_idx = 0
while True:
    time += 1
    
    # 뱀 이동
    if not move():
        break
    
    # 방향 변환
    if turn_idx < len(turns) and time == turns[turn_idx][0]:
        if turns[turn_idx][1] == 'D': # 오른쪽 회전
            direction = direction % 4 + 1
        else: # 왼쪽 회전
            direction = direction - 1 if direction > 1 else 4
        turn_idx += 1

# 결과 출력
print(time)

# source code: https://velog.io/@joniekwon/Python-%EB%B0%B1%EC%A4%80-3190%EB%B2%88-%EB%B1%80

# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# k = int(input())
# maps = [[0] * (n+1) for _ in range(n+1)]
# for _ in range(k):#사과의 위치
#     x,y = map(int,input().split())
#     maps[x][y] = 2
# info = {}
# l = int(input())
# for _ in range(l):# 뱀의 방향변환정보 (초, 방향 L:왼쪽 D:오른쪽)
#     sec, direct = input().split()
#     info[int(sec)] = direct
# time = 0
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# x, y = 1, 1
# maps[y][x] = 1
# d = 0
# snakes = deque([(1, 1)])

# while True:
#     nx, ny = x+dx[d], y+dy[d]
#     # 뱀의 몸통에 닿거나 벽에 부딪히는 경우 종료
#     if nx<=0 or ny<=0 or nx>n or ny>n or (nx,ny) in snakes:
#         break
#     # 사과를 먹지 못하면 꼬리 없애기
#     if maps[ny][nx]!=2:
#         a,b = snakes.popleft()
#         maps[b][a]=0
#     x, y = nx, ny
#     maps[y][x] = 1
#     snakes.append((nx, ny))
#     time+=1
	
#     # 시간에 해당하는 방향전환 정보가 있을 경우
#     if time in info.keys():
#         if info[time] == "D":
#             d = (d+1)%4
#         else:
#             nd = 3 if d==0 else d-1
#             d = nd
# print(time+1)
