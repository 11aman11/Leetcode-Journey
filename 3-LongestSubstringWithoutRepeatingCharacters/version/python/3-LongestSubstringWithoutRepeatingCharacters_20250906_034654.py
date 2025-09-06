# Last updated: 9/6/2025, 3:46:54 AM
# so i first used hashset instead of hashmap dict but if use hashmap then find the invalid > 1 and keep removing dw about delete because we care about the length movement of right and left
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = left = 0
        # curr = defaultdict(dict)
        # curr = set()
        curr = defaultdict(int)

        for right in range(len(s)):
        #     while s[right] in curr:
        #         curr.remove(s[left])
        #         # curr[s[left]] -= 1
        #         left += 1
        #     # curr[s[right]] += 1
        #     curr.add(s[right])
        #     ans = max(ans, len(curr))
        # return ans
        # p l=0 ans= 0 r=0 set(p)
        # w l=0 r= 1 set(p, w) ans = 2
        # w l= 1 r = 2 set(w) ans = 2
        # k l= 1 r = 3 set(w, k) ans = 3
        # e l= 1 r= 4 set(w,k,e) ans = 4
            curr[s[right]] += 1
            while curr[s[right]] > 1:
                curr[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


            
            
        