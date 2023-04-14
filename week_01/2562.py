nums = []
for i in range(9):
    nums.append(int(input()))

max_num = max(nums)
max_idx = nums.index(max_num) + 1

print(max_num)
print(max_idx)
