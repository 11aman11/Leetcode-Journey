# Last updated: 8/30/2025, 5:57:40 PM
# better time complexity
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


        freq = defaultdict(int)
        for key in len(s):
            freq[key] += 1
        
        return sort(set(freq.values())) == 1













        map = defaultdict(int)
        for key in s:
            map[key] += 1
        return set(map.values()) == 1