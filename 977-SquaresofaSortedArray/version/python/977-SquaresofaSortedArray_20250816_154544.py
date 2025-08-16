# Last updated: 8/16/2025, 3:45:44 PM
# very tricky please come back and do better mistkes: <=, space complextiy, put it backwards in the list without any functions
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        out = [0] * len(nums)
        write = len(nums) - 1
        
        while (left <= right):
            lv = nums[left] **2
            rv = nums[right] **2
            if lv < rv:
                out[write] = rv
                right -= 1
            else:
                out[write] = lv
                left += 1
            write -= 1                  
        return out
        # n = len(nums)
        # out = [0] * n  # Pre-allocated list
        # left, right = 0, n - 1
        # write = n - 1  # Start writing from the end

        # while left <= right:
        #     lv = nums[left] ** 2
        #     rv = nums[right] ** 2

        #     if lv > rv:
        #         out[write] = lv
        #         left += 1
        #     else:
        #         out[write] = rv
        #         right -= 1

        #     write -= 1  # Move write pointer backward

        # return out
