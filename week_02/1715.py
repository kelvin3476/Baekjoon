# source code: https://velog.io/@dding_ji/baekjoon-1715
from heapq import heappush, heappop
import sys
heap = []
result = 0

for i in range(int(sys.stdin.readline())):
    heappush(heap, int(sys.stdin.readline()))

while len(heap) > 1:
    plus = heappop(heap) + heappop(heap)
    result += plus
    heappush(heap, plus)
print(result)