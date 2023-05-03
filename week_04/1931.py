import sys

input = sys.stdin.readline

n = int(input()) # 회의의 수
times = [list(map(int, (input().split()))) for i in range(n)] # 회의 시간
times.sort(key = lambda x: (x[1], x[0])) # 각 회의 종료 시간을 기준으로 정렬

cnt = 1 # 회의의 개수 1로 초기화

for i in range(1, n): # (1부터 n만큼)
    if times[0][1] <= times[i][0]: # 다음회의 시작시간이 현재회의 종료시간이 이후이면 
        cnt += 1 
        times[0][1] = times[i][1] # 다음회의 종료시간을 현재회의 종료시간으로 업데이트 해준다.

print(cnt) # 회의의 개수 출력