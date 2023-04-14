input() # 입력받을 숫자의 개수
data = list(map(int, input().split())) # 공백으로 숫자 구분. ex) 1 3 5 7
totalcount = 0 # 소수의 개수

for i in data:
    count = 0 
    if(i == 1): # 1은 소수가 아니기 때문에 건너띔
        continue
    for j in range(2, i+1):
        if(i % j == 0):
            count += 1
    if(count == 1):
        totalcount += 1
print(totalcount)