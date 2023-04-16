# n = int(input())
# l = [list(map(int, input().split())) for _ in range(n)]
# visit = [0] * n
# m = 1e9

# def dfs(depth, start, cost):
#     global m
#     if depth == n-1 and l[start][0] != 0:
#         m = min(m, cost+l[start][0])
#         return
#     for i in range(n):
#         if not visit[i] and l[start][i] != 0:
#             visit[i] = 1
#             dfs(depth+1, i, cost+l[start][i])
#             visit[i] = 0
# visit[0] = 1
# dfs(0, 0, 0)
# print(m)

# N = int(input()) #도시의 개수
# travel_cost = [list(map(int, input().split())) for _ in range(N)]
# min_value = 1000000000 #출력할 최소값 정의

# def dfs_backtracking(current_city, next_city, cost, visited_city): #시작도시번호,다음도시번호,비용,방문 도시
#     global min_value

#     if len(visited_city) == N: #만약 방문한 도시가 입력받은 도시의 개수라면
#         if travel_cost[next_city][current_city] != 0: #마지막 도시에서 출발 도시로 가는 비용이 0이 아니라면(즉,갈수 있다면)
#             min_value = min(min_value, cost + travel_cost[next_city][current_city]) #더한 값을 저장되어있는 최소값과 비교해서 대입
#             return
#     for i in range(N): #도시의 개수 만큼 반복문을 돈다.
#         #만약 현재 도시에서 갈 수 있는 도시의 비용이 0이 아니고 이미 방문한 도시가 아니며 그 비용값이 저장되어있는 최소값보다 작다면
#         if travel_cost[next_city][i] != 0 and i not in visited_city and cost < min_value: 
#             visited_city.append(i) #그 도시를 방문목록에 추가
#             dfs_backtracking(current_city, i, cost + travel_cost[next_city][i], visited_city) #그 도시를 방문한다.
#             visited_city.pop() #방문을 완료했다면 방문목록 해제


# #도시마다(0~3) 출발점을 지정
# # for i in range(N):
#     # dfs_backtracking(i, i, 0, [i])
#     dfs_backtracking(i, i, 0, [i])

# print(min_value)

import sys

def dfs(current, cost, cnt):
    global min_cost
    if cnt == N: #마지막에서 다시 처음으로 돌아가야함
        if a[current][0]: #현재도시에서 처음 도시로
            cost += a[current][0] #값을 더함
            if min_cost > cost: #비교
                min_cost = cost #미니멈이 순회비용보다 크면 순회비용이 미니멈이 됨
        return #리턴

    if cost > min_cost: #방문을 다 하기전에 값이 미니멈보다 크면 리턴 즉 다른 도시로 갈수 없다.
        return

    for i in range(N):  
        if not visited[i] and a[current][i]: #1-4, 이미 도시 0은 방문처리완료 현재 도시에서부터 i 도시
            visited[i] = True #방문처리 완료
            dfs(i, cost + a[current][i], cnt + 1) #재귀를 이용해서 시작도시, 다음도시, 벨류라는 변수에 저장, 방문도시 체크
            visited[i] = False #도시 리셋

N = int(input()) #input 값을 받음 # 4
a = [list(map(int, input().split()))for _ in range(N)] #이차원적 리스트를 생성 [[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]] 
min_cost = 1000000000 #변수 미니멈을 최대값으로 생성
visited = [False] * N #도시의 수만큼 False라는 인덱스 생성 [False, False, False, False] 
visited[0] = True # 시작 도시는 무조건 True
dfs(0, 0, 1) 
print(min_cost)
