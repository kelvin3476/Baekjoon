x, y, w, h = map(int, input().split())

distances = [x,y,w - x, h - y] # 각 변과의 거리 계산
min_distance = min(distances) # 가장 짧은 거리 계산

print(min_distance)