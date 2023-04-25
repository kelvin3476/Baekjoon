# source code: https://backtony.github.io/algorithm/2021-02-18-algorithm-boj-class4-20/

import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline # [50, 30, 24, 5, 28, 45, 98, 52, 60]


def post_order(start, end): 
    # 역전시 리턴
    if start > end: 
        return

    # 루트 노드
    root = pre_order[start] # root = 50, root = 30, root = 24, root = 5, root = 28, root = 45, root = 98, root = 52, root = 60 # vertex
    idx = start + 1  # idx = 1, idx = 2, idx = 3, idx = 4, idx = 5, idx = 6, idx = 7, idx = 8, idx = 9 # vertex 의 인덱스 번호

    # root보다 커지는 지점을 찾는 과정  
    # for문으로 찾으면 안된다. 아래서 설명  
    while idx <= end: 
        if pre_order[idx] > root: 
            break
        idx += 1 

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1) 
    # 오른쪽 서브트리
    post_order(idx, end)
    # 후위순회이므로 제일 마지막에 찍으면 된다
    print(root) # [5, 28, 24, 45, 30, 60, 52, 98, 50]


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)