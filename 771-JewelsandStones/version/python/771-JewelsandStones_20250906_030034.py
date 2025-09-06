# Last updated: 9/6/2025, 3:00:34 AM
# lesgo with no mistake
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        mapS = defaultdict(int)
        
        for item in stones:
            mapS[item] += 1
        
        count = 0
        for stone in jewels:
            if stone in mapS:
                count += mapS[stone]
        return count
                