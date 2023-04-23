import sys

N = int(sys.stdin.readline()) # 8
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
blue = 0 
white = 0

def solution(x, y, N): # (x, y, N) == input값 ex) 0,0,8
    global white, blue
    color = board[x][y] # color = 보드판 x, y 좌표
    for i in range(x, x+N): # (x, x+N) => 가로 좌표, 즉 i = 0 일때 x[0] = (0.0) 
        for j in range(y, y+N): # (y, y+N) => 세로 좌표, 즉 j = 0 일때 y[0] = (0,0)
            if color != board[i][j]: # if board[x][y] != board[i][j]
                solution(x, y, N//2) # solution(0, 0, 8//2) # 1사분면
                solution(x, y+N//2, N//2) # solution(0, 0+8//2, 8//2) # 3사분면
                solution(x+N//2, y, N//2) # solution(0+8//2, 0, 8//2) # 2사분면
                solution(x+N//2, y+N//2, N//2) # solution(0+8//2, 0+8//2, 8//2) 4사분면
                return
    if color == 0: # board[x,y] == 0
        white += 1
    else:
        blue += 1

solution(0, 0, N)
print(white)
print(blue)