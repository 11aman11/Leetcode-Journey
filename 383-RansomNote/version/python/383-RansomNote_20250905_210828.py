# Last updated: 9/5/2025, 9:08:28 PM
# mistakes: == but <=
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq1 = defaultdict(int)
        for c in magazine:
            freq1[c] += 1
        
        freq2 = defaultdict(int)
        for c in ransomNote:
            freq2[c] += 1
        
        for key in freq2:
            if freq2[key] > freq1[key]:
                return False
        return True
