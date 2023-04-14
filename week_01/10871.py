# 수열 A와 정수 X를 입력 받기
n, x = map(int, input().split())
# 수열 A를 입력 받기
a = list(map(int, input().split()))

# 수열 A에서 X보다 작은 수를 모두 출력하기
for n in a:
    if n < x:
        print(n, end=' ')