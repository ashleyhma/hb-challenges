def threeSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

    Note:

    The solution set must not contain duplicate triplets.
    """
    
    results = set()
    nums.sort()
    
    i = 0
    while i < len(nums) - 2:
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                results.add((nums[i], nums[j], nums[k]))
                j += 1 
                k -= 1 
            elif s > 0:
                k -= 1
            else:
                j += 1
        i += 1 
        
    return list(results)