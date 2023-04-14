N, M = map(int, input().split()) # N 나무의 개수, M 집에 가져가기 위한 나무의 미터 길이
tree = list(map(int, input().split())) # [20, 15, 10, 17]
start, end = 1, max(tree) #이분탐색 검색 범위 설정 [1, 20]

while start <= end: #적절한 벌목 높이를 찾는 알고리즘 # 1 <= 20
    mid = (start+end) // 2 # 10 = (1+20) // 2
    
    log = 0 #벌목된 나무 총합 (초기화)
    for i in tree: # [20, 15, 10, 17] => tree[0], tree[1], tree[2], tree[3]
        if i >= mid: # 20 >= 10
            log += i - mid # 10 += 20 - 10
    
    #벌목 높이를 이분탐색
    if log >= M: # 10 >= 7
        start = mid + 1 # 11 = 10 + 1
    else:
        end = mid - 1
print(end)