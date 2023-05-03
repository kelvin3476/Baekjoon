import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input()) # 지원자 수
    freshmen = [] # 신입사원 지원자 성적 및 순위 정보 리스트 

    for j in range(n):
        credit, rank = map(int, input().split()) # 성적, 순위
        freshmen.append((credit, rank))

    freshmen.sort() #서류 심사 성적을 기준으로 오름차순 정렬

    cnt = 1 # 선발할수 있는 신입사원 수
    interview = freshmen[0][1] # 순위

    for k in range(1, n):
        if freshmen[k][1] < interview: # 면접 심사 성적이 더 높은 사원이 있으면
            cnt += 1
            interview = freshmen[k][1] # 면접 심사 성적을 업데이트
    print(cnt)
