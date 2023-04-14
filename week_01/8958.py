T = int(input())

result = ''

for i in range(T):
    list = input()
    score = 0
    sum = 0
    for j in range(len(list)):
        if list[j] == 'O':
            score += 1
        else: 
            score = 0

        sum += score
    result += (f'{sum}\n')
print(result)