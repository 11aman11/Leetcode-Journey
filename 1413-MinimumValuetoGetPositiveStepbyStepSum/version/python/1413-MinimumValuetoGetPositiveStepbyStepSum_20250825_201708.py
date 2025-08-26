# Last updated: 8/25/2025, 8:17:08 PM
# Better Solution in terms of understanding as well as not changing the nums when you don't have to
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # minSum = nums
        # for i in range(1, len(nums)):
        #     nums[i] = nums[i] + nums[i - 1]
        #     minSum = min(minSum, nums[i])

        # startV = abs(minSum) + 1
        # return startV

        minSum = 0
        total = 0
        for num in nums:
            total += num
            minSum = min(total, minSum)
        
        return abs(minSum) + 1
        # hint step by step sum is to find minium prefix sum add plus 1 to find the start value and mistakes i couldn't know what to do
        # i forgot to add 1 becuase this is the lowest start value 