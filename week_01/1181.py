import sys

n = int(sys.stdin.readline())
dic = []

for i in range(n):
    dic.append(sys.stdin.readline().strip())
set_dic = set(dic)
dic = list(set_dic)
dic.sort()
dic.sort(key = len)
for i in dic:
    print(i)

# import sys
# input = sys.stdin.readline()
# N = int(input())
# word_list= []
# sorted_word = []

# for i in range(N):
#     a =(input())
#     word_list.append(a.rstrip())
    
# set_word = list(set(word_list))
# for i in set_word:
#     sorted_word.append((len(i), i))

# result = sorted(sorted_word)

# for num, word in result:
#     print(word)   