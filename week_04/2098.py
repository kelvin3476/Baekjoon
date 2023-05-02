# 하향식 풀이법(Top-Down)
import sys
INF = sys.maxsize  # 무한대 값으로 초기화
def tsp(curr, visited):
    # 모든 도시를 방문한 경우, 현재 도시에서 출발 도시로 돌아가는 비용을 반환
    if visited == (1 << N) - 1: # 1 == 15 # 3 == 15 
        return graph[curr][0] if graph[curr][0] > 0 else INF
    # 이미 계산한 값이 있는 경우, 바로 반환
    if dp[curr][visited] != -1:
        return dp[curr][visited]
    # 최소 비용으로 도시를 방문하는 경로를 찾음
    result = INF
    for i in range(1, N):
        # 이미 방문한 도시는 건너뛰기
        if visited & (1 << i):
            continue
        # 현재 도시에서 다음 도시로 이동하는 비용
        cost = graph[curr][i]
        if cost == 0:
            continue
        # 다음 도시를 방문한 경우의 비용 계산
        next_visited = visited | (1 << i)
        next_cost = cost + tsp(i, next_visited)
        # 최소 비용 갱신
        result = min(result, next_cost)
    # 결과 저장 후 반환
    dp[curr][visited] = result
    return result
N = int(input())  # 도시의 개수
graph = [list(map(int, input().split())) for _ in range(N)]  # 비용 그래프
# 메모이제이션을 위한 DP 테이블 초기화
dp = [[-1] * (1 << N) for _ in range(N)]
# 출발 도시는 0번 도시로 고정
start = 0
visited = 1 << start
# 최소 비용으로 모든 도시를 방문하는 경로를 찾음
answer = tsp(start, visited)
print(answer)
