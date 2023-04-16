A, B, V = map(int, input().split())
 
n = V - A
if n % (A-B) == 0:
    count = int(n/(A-B))
else:
    count = int(n//(A-B) + 1)
print(count + 1)

A, B, V = map(int, input().split()) # 2 1 5
 
n = V - A # n = 5 - 2
if n % (A-B) == 0: # 3 % (2 - 1) == 0 
    count = int(n/(A-B)) # count =(3/(2 - 1))
else:
    count = int(n/(A-B) + 1)
print(count + 1) # count + 1 = 4