# Last updated: 8/25/2025, 7:27:33 PM
# mistakes: use append properly, [-1] to access the last element and to add them with the previous while putting it prefix array, don't forget range starts from 1 as you first element is already in prefix
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        return prefix