# Last updated: 8/26/2025, 8:11:07 PM
# did a silly mistake where instead of while > k i wrote while > 2, careful with the constant value to be replaced with variable
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #mistakes lot many

        # left = ans = curr = 0 
        # for right in range(len(nums)):
        #     if nums[right] == 0:
        #         curr += 1

        #     while curr > k:
        #         if nums[left] == 0:
        #             curr -= 1
        #         left += 1
        #     ans = max(ans, right - left + 1)
        # return ans

        left = ans = curr = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                curr += 1
            
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans