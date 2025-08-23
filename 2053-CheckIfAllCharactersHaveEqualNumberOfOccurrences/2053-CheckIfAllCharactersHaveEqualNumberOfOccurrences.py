# Last updated: 8/23/2025, 3:51:41 PM
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = defaultdict(int)
        for char in s:
            freq [char] += 1

        times = freq[s[0]]

        # for key in freq:
        #     if freq[key] != times:
        #         return False
        # return True    

        #smarter way instead of for
        times = freq.values()
        return len(set(times)) == 1
