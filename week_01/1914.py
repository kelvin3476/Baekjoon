n =  int(input())

def Hanoi(n, x, y):
    if n == 1:
        print(x, y)
        return
    Hanoi(n-1, x, 6-x-y)
    print(x, y)
    Hanoi(n-1, 6-x-y, y)

print(2 ** n - 1)

if n <= 20: Hanoi(n, 1, 3)