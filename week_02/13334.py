#source code: https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-13334-%EC%B2%A0%EB%A1%9C%ED%8C%8C%EC%9D%B4%EC%8D%AC
#lambda reference: https://gorokke.tistory.com/38
import sys
import heapq

n = int(sys.stdin.readline()) # n = 8
road_info = [] 
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

d = int(sys.stdin.readline()) # 30
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)