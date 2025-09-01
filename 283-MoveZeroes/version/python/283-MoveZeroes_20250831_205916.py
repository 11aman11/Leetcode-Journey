# Last updated: 8/31/2025, 8:59:16 PM
# chatgpt
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

# fill remaining with zeros
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1

        return nums

           