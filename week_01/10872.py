N  = int(input())
    
def fact(N):
    if N == 0:      # n이 0일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return N * fact(N - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
print(fact(N))