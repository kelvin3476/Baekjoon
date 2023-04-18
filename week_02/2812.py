import sys
input = sys.stdin.readline

N, K = map(int, (input().split()))
L = N - K
stack = []
num = input()

for i in range(N):
    while True:
        if stack and num[i] > stack[-1] and K > 0:
            stack.pop()
            K -= 1
        else:
            break
    
    stack.append(num[i])

for i in range(L):
    print(stack[i], end='')
    