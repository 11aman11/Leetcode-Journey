# Last updated: 8/23/2025, 3:51:43 PM
class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nums = set(arr)
        freq = 0
        for i in range(len(arr)):
            if (arr[i] + 1) in nums:
                freq += 1
        return freq