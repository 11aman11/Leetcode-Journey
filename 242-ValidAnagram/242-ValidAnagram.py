# Last updated: 8/23/2025, 3:51:48 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    # listS = sorted(s)
        # listT = sorted(t)
        # if len(listS) == len(listT):
        #     for index in range(len(listS)):
        #         if listS[index] != listT[index]:
        #             return False
        #     return True
        # else:
        #     return False

        #optimal
        # if len(s) == len(t):
        #     hash1 = {}
        #     for letter in s:
        #         if letter in hash1:
        #             hash1[letter] += 1
        #         else:
        #             hash1[letter] = 1

        #     hash2 = {}
        #     for letter in t:
        #         if letter in hash2:
        #             hash2[letter] += 1
        #         else:
        #             hash2[letter] = 1

        #     return True if hash1 == hash2 else False
        # else:
        #     return False
        if len(s) == len(t):
            check = {}
            for char in s:
                if char in check:
                    check[char] += 1
                else:
                    check[char] = 1

            for char in t:
                if char in check:
                    check[char] -=1
                else:
                    check[char] = 1

            for key in check.values():
                if key != 0:
                    return False
            return True
        else:
            return False     