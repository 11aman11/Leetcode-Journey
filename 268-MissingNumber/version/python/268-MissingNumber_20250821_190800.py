# Last updated: 8/21/2025, 7:08:00 PM
# mistake: use i as index to check in set
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
        