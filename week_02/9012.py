import sys
T = int(sys.stdin.readline())

for _ in range(T):
    command = sys.stdin.readline()
    stack = []

    for i in command:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')