import sys
# https://wonyoung2257.tistory.com/79 참고
N = int(sys.stdin.readline())
circles = []
for i in range(N) :
    x, r = map(int, sys.stdin.readline().split())
    circles.append((x-r, '(')) # 중점을 기준으로 왼쪽에 있는 좌표
    circles.append((x+r, ')')) # 중점을 기준으로 오른쪽에 있는 좌표
# x좌표 순으로 오름차순 정렬 & 같을 경우 ')' 문자를 가진 값이 앞으로 오도록
# 아스키 코드 : '(' = 72, ')' = 73
circles.sort(key = lambda x: (x[0], -ord(x[1])))
# {좌표, 괄호모양, 상태값}
# 상태값 = 0 : 뒤의 원과 접해 있지 않는다. / 1 : 뒤의 원과 접한다.
stack = []
result = 1
# 왼쪽, 오른쪽 저장을 따로 했기에 N*2번 반복
for i in range(N*2) :
    x, y = circles[i] # x: 좌표, y: 괄호
    # 스택이 비어있을 경우에는 무조건 push
    if len(stack) == 0 :
        stack.append({'x' : x, 'y' : y, "status" : 0})
    # 스택에 값이 존재할 경우
    else :
        # 괄호가 ')' 이면 원이 무조건 완성
        if y == ')' :
            # 원이 다른 원과 접해있지 않을 경우
            if stack[-1]['status'] == 0 :
                result += 1
            # 원이 다른 원과 접해있을 경우
            elif stack[-1]['status'] == 1 :
                result += 2
            # 앞에 사용한 '(' 값 pop
            stack.pop()
            #현재 완성된 원이 다음 원과 접해있는지 확인
            if i != N*2-1 :
                if circles[i+1][0] != x :
                    stack[-1]['status'] = 0
        # 괄호 '('일 경우
        else :
            # 접해있을 경우 상태 변경
            if stack[-1]['x'] == x :
                stack[-1]['status'] = 1
            stack.append({'x' : x, 'y' : y, "status" : 0})
print(result)