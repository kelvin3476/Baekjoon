import sys
K = int(sys.stdin.readline())

stack = []

for i in range(K):
    command = int(sys.stdin.readline())
    if command == 0:
        stack.pop()
    else: 
        stack.append(command)

print(sum(stack))
