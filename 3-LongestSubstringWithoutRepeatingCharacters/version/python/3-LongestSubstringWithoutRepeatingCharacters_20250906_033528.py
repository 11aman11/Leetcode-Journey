# Last updated: 9/6/2025, 3:35:28 AM
# let's goooooo
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = left = 0
        # curr = defaultdict(dict)
        curr = set()

        for right in range(len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                # curr[s[left]] -= 1
                left += 1
            # curr[s[right]] += 1
            curr.add(s[right])
            ans = max(ans, len(curr))
        return ans
        # p l=0 ans= 0 r=0 set(p)
        # w l=0 r= 1 set(p, w) ans = 2
        # w l= 1 r = 2 set(w) ans = 2
        # k l= 1 r = 3 set(w, k) ans = 3
        # e l= 1 r= 4 set(w,k,e) ans = 4
        #
        #
            

            
            
        