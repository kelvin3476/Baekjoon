a, b = input().split()
reverse_A = int(a[2]+a[1]+a[0])
reverse_B = int(b[2]+b[1]+b[0])

print(max(reverse_A, reverse_B))