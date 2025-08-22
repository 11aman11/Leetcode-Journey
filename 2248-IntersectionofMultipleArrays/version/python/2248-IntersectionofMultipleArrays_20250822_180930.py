# Last updated: 8/22/2025, 6:09:30 PM
# try to use just each letter no need for index; mistakes: used else wrongly has not to be there, got stuck with looping over the keys, yea try speaking out loud
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
