r, c = map(int, input().split())
#자르는 위치 저장
row = [0, r]    # [0, 10]
column = [0, c] #  [0, 8] 

for _ in range(int(input())):   # 자르는 횟수
    r_or_c, linenumber = map(int, input().split())  
    if r_or_c == 1:             # 세로가 1 가로가 0-> 세로는 r에 가로는 c 
        row.append(linenumber)
    else :
        column.append(linenumber)

row.sort()     # [0, 4, 10]
column.sort()  # [0, 2, 3, 8]
               # 빼서 최대 길이 구하기

temp = 0

for i in range(len(row)-1):
    for j in range(len(column)-1):
        area = (row[i+1]-row[i])*(column[j+1]-column[j]) 
        if area > temp:
            temp = area 

print(temp)