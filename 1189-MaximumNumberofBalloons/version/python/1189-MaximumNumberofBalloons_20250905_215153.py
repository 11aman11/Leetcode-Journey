# Last updated: 9/5/2025, 9:51:53 PM
# mistake i did was misspelling balloon to ballon
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
            if c in countB:
                val = min(val, countB[c]/mapB[c])
            else:
                return 0
        return val

            
                