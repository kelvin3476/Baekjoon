import sys
input = sys.stdin.readline
shooting_stand, animal, distance = map(int, input().split()) #사대, 동물 수, 사정거리 4, 8, 4
shooting_stand_list = list(map(int, input().split())) #사대 좌표 [6, 1, 4, 9]
shooting_stand_list.sort() #정렬 [1, 4, 6, 9]
animals = [list(map(int, input().split())) for i in range(animal)] #동물들 x, y 좌표 
animals.sort()

count = 0
for x, y in animals: # x, y 에 동물 좌표
    start = 0
    end = len(shooting_stand_list) - 1 #사대의 개수로 범위 지정
    while start <= end: #이분탐색 종료 시점 (*** start <= end, start = end가 같을때에도 포함이 되어야 while 문이 돌아감)
        mid = (start + end) // 2 # 중간값
        if abs(shooting_stand_list[mid] - x) + y <= distance or abs(shooting_stand_list[mid-1] - x) + y <= distance: #end와 end-1은 a의 왼쪽 오른쪽 값 ㅣxj - ajㅣ + bj <= l 이면 동물을 잡은거니 count +1
            count += 1
            break
        if shooting_stand_list[mid] < x: #m_list의 중간 인덱스가 x보다 작으면 x보다 mid가 작으므로 스타트지점 옮김
            start = mid + 1
        else:
            end = mid - 1 #m_list의 중간 인덱스가 x보다 크면 끝지점 옮김  end의 위치가 x랑 가장 가까운 수가 됨
print(count)