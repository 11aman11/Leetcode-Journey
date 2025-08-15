# Last updated: 8/15/2025, 11:46:50 AM
# use 2 pointer to reverse or play it smart use function s.reverse() space O(n) while two pointer space O(1). time is O(n) both
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while (left < right):
            temp = s[left]
            s[left]= s[right]
            s[right] = temp
            left += 1
            right -= 1
        return s    


        