import sys
T = int(sys.stdin.readline())

result = '' 

for i in range(T): 
    n, s = input().split()
    n = int(n)
    p = ''
    for j in range(len(s)):
        p += s[j] * n
    result += f'{p}\n'
print(result)