import sys
N, C = map(int, sys.stdin.readline().split())
house = []
for i in range(N) :
    house.append(int(sys.stdin.readline()))
house.sort()
def wifi(house, c) :
    # 공유기를 설치할 수 있는 최소 거리, 최대 거리
    min_len, max_len = 1, house[N-1] - house[0]
    length = 0
    while min_len <= max_len :
        # 현재 공유기를 설치할 수 있는 거리
        mid_len = (min_len + max_len) // 2
        # 설치된 공유기 개수
        count = 1
        current = house[0]
        for i in range(1, N) :
            # 현재 위치에서 공유기를 설치할 수 있는 거리보다 멀리 있으면
            if current + mid_len <= house[i]:
                count += 1
                current = house[i]
        # 현재 설치된 공유기의 개수가 가지고 있는 공유기의 개수보다 많은 경우
        # 즉, 더 멀찍이 설치할 수 있다.
        if count >= c :
            min_len = mid_len + 1
            length = max(length, mid_len)
        # 현재 설치된 공유기의 개수가 가지고 있는 공유기의 개수보다 적은 경우
        # 설정된 거리가 너무 멀기에 좀 가까워져야한다.
        else :
            max_len = mid_len -1
    return length
print(wifi(house, C))