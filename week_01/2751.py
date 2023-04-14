import sys
sys.stdin.readline = input 
N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))
nums1 = sorted(nums)
for i in range(len(nums)):
    print(nums1[i])

