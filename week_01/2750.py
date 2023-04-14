N = int(input())                # T case: 5
nums = []                       # [] 
for i in range(N):
    nums.append(int(input()))   # [5, 2, 3, 4, 1]
nums1 = sorted(nums)            # [1, 2, 3, 4, 5]
for i in range(len(nums)):    
    print(nums1[i])             # [nums1[0], nums1[1], nums1[2], nums1[3], nums1[4]]