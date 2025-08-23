# Last updated: 8/23/2025, 3:51:42 PM
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        counts = defaultdict(int)
        for arr in nums:
            for i in range(len(arr)):
                counts[arr[i]] += 1
        
        out = []
        
        for key in counts.keys():
            if counts[key] == len(nums):
                out.append(key)
        return sorted(out)
