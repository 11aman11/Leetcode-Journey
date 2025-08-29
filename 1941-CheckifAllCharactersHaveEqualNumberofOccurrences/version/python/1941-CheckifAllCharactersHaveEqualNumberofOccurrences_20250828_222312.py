# Last updated: 8/28/2025, 10:23:12 PM
# since occurances thus build the map and use it for the probelm, return the len of set if its 1 then all had same values
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
















        map = defaultdict(int)
        for key in s:
            map[key] += 1
        return set(map.values()) == 1