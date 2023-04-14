A, B, V = map(int, input().split())
 
n = V - A
if n % (A-B) == 0:
    count = int(n/(A-B))
else:
    count = int(n//(A-B) + 1)
print(count + 1)