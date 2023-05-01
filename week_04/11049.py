# pypy3 만 통과 상향식 풀이법 (Bottom-Up)
# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# n = int(input()) # 행렬의 개수를 입력받음

# matrix = [] # 행렬의 크기를 저장할 리스트
# for _ in range(n):
#     r, c = map(int, input().split()) # 행렬의 크기를 입력받음
#     matrix.append((r, c)) # 입력받은 행렬의 크기를 리스트에 추가함

# dp = [[0] * n for _ in range(n)] # dp 테이블 초기화
# for i in range(1, n): # 행렬 곱셉의 길이를 1부터 n-1까지 반복
#     for j in range(0, n-i): # 시작하는 행렬의 인덱스를 0부터 n-i-1까지 반복
#         dp[j][j+i] = sys.maxsize # dp[j][j+i]를 최댓값으로 초기화
#         for k in range(j, j+i): # k를 j부터 j+i-1까지 반복
#             # dp[j][k]와 dp[k+1][j+i]를 더한 값과
#             # 행렬 j부터 j+i까지의 곱셈을 했을 때의 곱셈 연산 횟수를 곱한 값을
#             # dp[j][j+i]에 저장함
#             dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + matrix[j][0]*matrix[k][1]*matrix[j+i][1])

# print(dp[0][n-1]) # 행렬 0부터 n-1까지의 곱셈을 하는데 필요한 최소 곱셈 연산 횟수를 출력함

# pypy3 만 통과 하향식 풀이법 (Top-Down)
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def matrix_chain_multiplication(matrix, dp, i, j):
    if dp[i][j] < sys.maxsize:
        return dp[i][j]
    if i == j:
        dp[i][j] = 0
        return 0
    for k in range(i, j):
        dp[i][j] = min(dp[i][j], matrix_chain_multiplication(matrix, dp, i, k) + matrix_chain_multiplication(matrix, dp, k+1, j) + matrix[i][0]*matrix[k][1]*matrix[j][1])
    return dp[i][j]

n = int(input())
matrix = []
for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

dp = [[sys.maxsize] * n for _ in range(n)]
matrix_chain_multiplication(matrix, dp, 0, n-1)

print(dp[0][n-1])

