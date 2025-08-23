// Last updated: 8/23/2025, 3:51:48 PM
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end()); 
        if (s==t)
            return true;
        else
            return false;
    }
};