# Last updated: 8/11/2025, 7:29:35 AM
# hashset to get unique values in array, to check for duplicates easily or use set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Brute force
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        #     return False        
        # Time: O(n^2) and Space O(1)
        # Optimal 
        return True if len(set(nums)) < len(nums) else False