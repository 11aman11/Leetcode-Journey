# Last updated: 9/2/2025, 8:26:06 PM
# come back to this problem as this is difficult to understand the concept
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mapPrefix = defaultdict(int)
        mapPrefix[0] = 1

        ans = cur = 0
        for num in nums:
            cur += num
            ans += mapPrefix[cur - k]
            mapPrefix[cur] += 1
        return ans