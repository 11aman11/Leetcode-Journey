# Last updated: 8/23/2025, 3:51:41 PM
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
        