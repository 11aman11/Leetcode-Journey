# Last updated: 8/17/2025, 9:27:39 PM
# Needs Review as you can do it with if else or while, be careful with 2 while here as you did mistake last time thinking 2 while means O n^2 but it is O n
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        while (left < right):
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True    
        