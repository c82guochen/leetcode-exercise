def findDuplicate(nums: List):
	for e in nums:
		tmp = abs(e)
    if nums[tmp] < 0:
                return -nums[tmp]
            nums[tmp] = - nums[tmp]
            
        return -1

print(findDuplicate[3,1,3,4,2])