# Last updated: 9/3/2025, 2:01:59 PM
# it was not easy question so come back to this
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = cur = 0
        counts = defaultdict(int)
        counts[0] = 1
        for num in nums:
            cur += num % 2
            ans += counts[cur - k]
            counts[cur] += 1
        return ans