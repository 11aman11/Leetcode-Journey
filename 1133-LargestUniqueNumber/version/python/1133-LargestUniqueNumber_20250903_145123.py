# Last updated: 9/3/2025, 2:51:23 PM
# used hashmap to store the values then loop again to check and find the max
class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        maxI = -1
        for num in nums:
            if seen[num] == 1:
                maxI = max(num, maxI)
        return maxI