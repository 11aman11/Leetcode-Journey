# Last updated: 9/3/2025, 11:48:15 AM
# forgot to add intial value of 0 count in the prefix map
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = defaultdict(int)
        prefix[0] = 1
        ans = cur = 0
        for num in nums:
            cur += num
            ans += prefix[cur - k]
            prefix[cur] += 1
        return ans