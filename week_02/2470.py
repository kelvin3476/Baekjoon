n = int(input()) # 5

arr = list(map(int, input().split(' '))) # [-2, 4, -99, -1, 98]
arr.sort() # [-99, -2, -1, 4, 98]

left = 0
right = n-1 # 4 = 5-1

answer = abs(arr[left] + arr[right]) # ans = abs(-99 + 98) => 1 = abs(-1)
final = [arr[left], arr[right]] # final = [-99, 98] 


while left < right: # 0 ~ 4
    left_val = arr[left] # left_val = -99
    right_val = arr[right] # right_val = 98

    s = left_val + right_val # -1 = -99 + 98
  
    if abs(s) < answer: # abs(-1) < 1 => 1 < 1
        answer = abs(s)
        final = [left_val, right_val]
        if answer == 0:
          break
    if s < 0: # -1 < 0
        left += 1 # left += 1 => left[0] => left[1] 
    else:
        right -= 1 # right -= 1 => right[4] => right[3] ... right[2]

print(final[0], final[1]) # (-99, 98)