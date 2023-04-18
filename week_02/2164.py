import sys
from collections import deque

input = sys.stdin.readline

L = deque(x+1 for x in range(int(input())))

while len(L) != 1:
    L.popleft()
    L.append(L.popleft())

print(L[0])