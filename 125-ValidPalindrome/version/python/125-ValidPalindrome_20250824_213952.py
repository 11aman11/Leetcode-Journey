# Last updated: 8/24/2025, 9:39:52 PM
# mistakes: -1 in len, alnum not alum
class Solution(object):
    def isPalindrome(self, s):
        # """
        # :type s: str
        # :rtype: bool
        # """
        # left = 0
        # right = len(s) - 1
        # while (left < right):
        #     if not s[left].isalnum():
        #         left += 1
        #     elif not s[right].isalnum():
        #         right -= 1
        #     elif s[left].lower() != s[right].lower():
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True    
        



        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            