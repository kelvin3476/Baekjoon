# 입력
N = int(input()) # 5
A = list(map(int, input().split())) # [4, 1, 5, 2, 3]
M = int(input()) # 5
arr = list(map(int, input().split())) # [1, 3, 7, 9, 5]
A.sort()			# A 정렬 [1, 2, 3, 4, 5]

# arr의 각 원소별로 이분탐색
for i in arr:
    first, end = 0, N - 1		# first는 맨 앞, end는 맨 뒤
    cnt = 0		# 찾음 여부

    # 이분탐색 시작
    while first <= end:		# first가 end보다 커지면 다돌고 반복문 탈출
        mid = (first + end) // 2	# mid는 first와 end의 중간값
        if i == A[mid]:	# i(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
            cnt = 1	    # cnt 1 변경
            print(1)		# 1 출력
            break		# 반복문 탈출
        elif i > A[mid]:	# A[mid]가 num보다 작으면
            first = mid + 1	# first를 높임
        else:			# A[mid]가 num보다 크다면
            end = mid - 1	# end를 낮춤

    if not cnt:		# 찾지 못한 경우
        print(0)		# 0 출력

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# if i == 1 => [4,1,5,2,3]:
#     i = True # i = 1, True = 1
# if i == 3 => [4,1,5,2,3]:
#     i = True # i = 3, True = 1
# if i == 7 => [4,1,5,2,3]:
#     i = False # i = 7, False = 0
# if i == 9 => [4,1,5,2,3]:
#     i = False # i = 9, False = 0
# if i == 5 => [4,1,5,2,3]:
#     i = True # i = 5, True = 1