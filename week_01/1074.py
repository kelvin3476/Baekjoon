N, row, column = map(int, input().split())

def solve(N, row, column):

	if N == 0:
		return 0
	return 2*(row%2)+(column%2) + 4*solve(N-1, int(row/2), int(column/2))

print(solve(N, row, column))