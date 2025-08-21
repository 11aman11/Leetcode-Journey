# Last updated: 8/21/2025, 7:01:40 PM
# did mistake lot in this silly: - you can iterate over set or dict with seen[i] as they are not idexed, also used string with alphabets instead just add the check if return == 26 alphabets
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        # seen = (string.ascii_lowercase)
        # seen = set(seen)
        # print(seen)
        # for char in seen:
        #     if  char not in sentence:
        #         return False
        # return True
        seen = set()
        for i in range(len(sentence)):
            if sentence[i] not in seen:
                seen.add(sentence[i])
        return len(seen) == 26
        