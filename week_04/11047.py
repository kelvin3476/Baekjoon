import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for i in range(n):
    coins.append(int(input()))

count = 0 # 동전 개수의 최솟값 초기화
    
for i in reversed(range(n)): # 동전의 가치가 큰것부터 시작
    if k == 0: # 동전 가치의 합이 0이 될때 break
        break
    if coins[i] <= k: # 해당 동전의 가치가 동전 가치의 합보다 작을때
        count += k // coins[i] # count에 동전 가치의 합을 해당 동전의 가치로 나눈 몫을 저장한다
        k %= coins[i] # k에 동전 가치의 합을 해당 동전의 가치로 나눈 나머지로 다시 저장한다.

print(count) # 동전 개수의 최솟값을 출력