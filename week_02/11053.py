import sys 

# A의 크기
N = int(sys.stdin.readline()) # 6
# 수열
A = list(map(int, sys.stdin.readline().split())) # [10, 20, 10, 30, 20, 50]
# https://namu.wiki/w/최장%20증가%20부분%20수열#s-3.2 참고
def LIS() :
    # d[i] = A[i]를 마지막 값으로 가지는 가장 긴 증가부분 수열 길이
    d = [A[0]] #[10]
    for i in range(1, len(A)) : # 1 ~ 6
        # d에 저장된 가장 마지막 값보다 현재 값이 크면
        if d[-1] < A[i] : # d[-1] < A[1]=> 10 < 20         20 < 10
            d.append(A[i]) # [10, 20]
        # 마지막 값보다 현재 값이 작으면
        # -> 0 ~ len(d)-1 사이에서 현재값보다 작은 값 중 가장 큰 값을 찾는다  -> 이분탐색
        else :
            min, max = 0, len(d)-1  # 2-1 = 1
            save = 0
            while min <= max : # 0 <= 1
                mid = (min + max) // 2 # mid = 0
                if d[mid] < A[i] : # 10 < 10
                    min = mid + 1 
                else :
                    max = mid -1 # max = -1
                    save = mid # save = 0
            d[save] = A[i] # d[0] = 10
    # 최종적으로 구해야하는 값
    print(len(d))
LIS()