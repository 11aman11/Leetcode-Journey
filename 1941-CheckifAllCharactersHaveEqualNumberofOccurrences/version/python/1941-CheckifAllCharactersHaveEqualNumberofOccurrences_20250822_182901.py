# Last updated: 8/22/2025, 6:29:01 PM
# i had tradeoff using for loop for extra time complexity while the submitted LeetCode solution had better time complexity.
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
