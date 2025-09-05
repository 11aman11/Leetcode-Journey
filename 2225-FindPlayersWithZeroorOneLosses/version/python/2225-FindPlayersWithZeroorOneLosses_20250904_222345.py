# Last updated: 9/4/2025, 10:23:45 PM
# did it any way but make sure the mistakes i did was [[][]], wrong 2 loops understanding, unpacking is o(1) since 2 constant elements
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        freqL = defaultdict(int)
        players = set()

        for w, l in matches:
            freqL[l] += 1
            players.add(w)
            players.add(l)

        ans = [[], []]
        for player in players:
            if player not in freqL:
                ans[0].append(player)        # 0 losses
            elif freqL[player] == 1:
                ans[1].append(player)        # 1 loss

        ans[0].sort()
        ans[1].sort()
        return ans
                    
                    
                