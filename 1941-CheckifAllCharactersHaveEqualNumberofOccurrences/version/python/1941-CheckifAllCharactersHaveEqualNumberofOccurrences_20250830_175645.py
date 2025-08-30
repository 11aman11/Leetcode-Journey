# Last updated: 8/30/2025, 5:56:45 PM
# did it again
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
        check = sort(set(freq.values()))
        return check == 1













        map = defaultdict(int)
        for key in s:
            map[key] += 1
        return set(map.values()) == 1