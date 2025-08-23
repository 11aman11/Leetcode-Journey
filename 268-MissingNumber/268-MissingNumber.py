# Last updated: 8/23/2025, 3:51:47 PM
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
        