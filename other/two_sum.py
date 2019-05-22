def twoSum(nums, target):
    """
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    """ 
    dic = {}
    
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[target - nums[i]] = i
        else:
            return dic[nums[i]], i