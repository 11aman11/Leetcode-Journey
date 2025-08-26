# Last updated: 8/25/2025, 8:04:41 PM
'''
hint step by step sum is to find minium prefix sum add plus 1 to find the start value and mistakes i couldn't know what to do
i forgot to add 1 becuase this is the lowest start value
'''

class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minSum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            minSum = min(minSum, nums[i])

        startV = abs(minSum) + 1 if minSum < 0 else 1
        return startV
        # hint step by step sum is to find minium prefix sum add plus 1 to find the start value and mistakes i couldn't know what to do
        # i forgot to add 1 becuase this is the lowest start value 