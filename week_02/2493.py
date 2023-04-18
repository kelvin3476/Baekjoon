N = int(input()) # 탑의 수 5
tops = list(map(int, (input().split()))) # 탑의 높이 6 9 5 7 4
answer = [0] * N # 수신 가능한 탑들을 저장할 스택 0 0 2 2 4
stack = [] # 각 탑의 수신 가능한 탑의 번호를 저장할 리스트 [1, 3, 4]

for i in range(N): 
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1] + 1
    
    stack.append(i)

print(*answer)