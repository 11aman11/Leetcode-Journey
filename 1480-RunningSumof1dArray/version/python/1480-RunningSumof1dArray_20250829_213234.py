# Last updated: 8/29/2025, 9:32:34 PM
# did it again
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # extra space
        # prefix = [nums[0]]
        # for i in range(1, len(nums)):
        #     prefix.append(nums[i] + prefix[-1])
        # return prefix   
        
        # in place
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
        return nums


        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i -1]
        return nums











