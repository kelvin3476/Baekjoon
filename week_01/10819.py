# https://sdesigner.tistory.com/51 <= source code
# https://datalabbit.tistory.com/42 <= permutations

# from itertools import permutations
# import sys 

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# per = list(permutations(A))
# max_value = 0    
# print(per)

# for i in per:
#     s = 0
#     for j in range(len(i)-1):
#         s += abs(i[j]-i[j+1])
#     if s > max_value:
#         max_value = s

# print(max_value)

# https://wonyoung2257.tistory.com/77 <= source code

n = int(input()) # 6
in_list = list(map(int ,input().split())) # [20, 1, 15, 8, 4, 10]
visited = [False]*n # [False, False, False, False, False, False]
answer = 0

def solve(new_list):
  global answer
  if len(new_list) == n:
    total = 0
    for i in range(n-1):
      total += abs(new_list[i]- new_list[i+1])
    answer = max(answer, total)
    return

  for i in range(n):
    if not visited[i]:
      visited[i] = True
      new_list.append(in_list[i])
      print("append",i,new_list)
      print()
      solve(new_list)
      visited[i] = False
      new_list.pop()
      print("pop",i,new_list)
      print()

solve([])
print(answer)
