# source code: https://velog.io/@ohk9134/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-python-%ED%8A%B8%EB%A6%AC-%EA%B5%AC%ED%98%84
# tree의 개념: https://m.blog.naver.com/rlakk11/60159303809

import sys

N = int(sys.stdin.readline().rstrip())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='') # root
        preorder(tree[root][0]) # left
        preorder(tree[root][1]) # right

def inorder(root):
    if root != '.':
        inorder(tree[root][0]) # left
        print(root, end='') # root
        inorder(tree[root][1]) # right

def postorder(root):
    if root !='.':
        postorder(tree[root][0]) # left
        postorder(tree[root][1]) # right
        print(root, end='') # root

preorder('A')
print()
inorder('A')
print()
