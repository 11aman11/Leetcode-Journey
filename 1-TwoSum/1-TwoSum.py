# Last updated: 8/23/2025, 3:51:51 PM
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return []

    
        seen = {}
        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[val] = i
        return []
            
        