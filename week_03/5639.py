import sys

# default 값이 1000이다
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline # [50, 30, 24, 5, 28, 45, 98, 52, 60]


def post_order(start, end): # (0,8) (1,1) (2,1) (3,2) (4,3) (5,4) (6, 4)
    # 역전시 리턴
    if start > end: 
        return

    # 루트 노드
    root = pre_order[start] # root = 50, root = 30, root = 24, root = 5, root = 28, root = 45, root = 98
    idx = start + 1  # idx = 1, idx = 2, idx = 3, idx = 4, idx = 5, idx = 6, idx = 7

    # root보다 커지는 지점을 찾는 과정  
    # for문으로 찾으면 안된다. 아래서 설명  
    while idx <= end: # 1 <= 8, 2 <= 1, 3 <= 1, 4 <= 2 5 <= 3 6 <= 4 7 <= 4
        if pre_order[idx] > root: # 30 > 50
            break
        idx += 1 # idx = 2 

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1) # (1, 1) (2, 1) (3, 2) (4, 3) (5, 4) 
    # 오른쪽 서브트리
    post_order(idx, end) # (6, 4)
    print(root)
    # 후위순회이므로 제일 마지막에 찍으면 된다
    # print(root) # [5, 28, 24, 45, 30, 60, 52, 98, 50]


pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    # try에서 예외 발생시 break 실행
    except:
        break

post_order(0, len(pre_order) - 1)