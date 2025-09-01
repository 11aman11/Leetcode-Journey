# Last updated: 9/1/2025, 7:40:05 PM
# using 2 pointer approach where we had o(n) time and space
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] **2
                left += 1
            else:
                result[i] = nums[right] **2
                right -= 1
        return result
        
                 
        