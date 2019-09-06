print('*******************************')
print('FIND THE LARGEST NO. IN A LIST')
print('*******************************')
nums = [540, 3500, 4596]
max = nums[0]
for x in nums:
  if x > max:
    max = x
print(max)