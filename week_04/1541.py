import sys

input = sys.stdin.readline

formula = input().split('-') # 입력 받는 수식 에서 '-' 기호 기준 으로 나눔

ans = 0 # 정답값 초기화
for i in formula[0].split('+'): # 수식의 0번째 인덱스에 있는 문자열을 '+' 기호 기준으로 나눔
    ans += int(i) # ans에 수식의 0번째 인덱스에 있는 i를 정수화 시킨후 더한다.

for i in formula[1:]: # 수식의 1번째 인덱스 부터 시작하는 문자열
    for j in i.split('+'): # 수식의 1번째 인덱스의 i 문자열을 '+' 기호 기준으로 나눔
        ans -= int(j) # ans에 수식의 1번째 인덱스의 i 문자열을 '+' 기호 기준으로 나눈 문자열 j를 정수화 시킨후 뺀다.

print(ans) # 정답값 출력