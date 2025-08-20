# Last updated: 8/20/2025, 2:35:17 PM
# fixed window!
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = ans = 0
        for i in range(k):
            curr += nums[i]
        
        ans = float(curr)/k
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            avg = float(curr)/k
            ans = max(avg, ans)
        return ans