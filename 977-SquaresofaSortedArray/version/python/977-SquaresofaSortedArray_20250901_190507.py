# Last updated: 9/1/2025, 7:05:07 PM
# brute force
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)