# Last updated: 9/5/2025, 10:05:00 PM
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        countB = defaultdict(int)
        for c in text:
            countB[c] += 1
        times = 0
        mapB = defaultdict(int)
        for c in "balloon":
            mapB[c] += 1
        val = float('inf')
        for c in mapB:
            val = min(val, countB[c]/mapB[c])
        return val

            
                