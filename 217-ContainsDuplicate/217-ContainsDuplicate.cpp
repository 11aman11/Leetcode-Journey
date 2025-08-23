// Last updated: 8/23/2025, 3:51:51 PM
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        
        int check=5;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++)
        {
            int find=nums[i];
             nums.erase(nums.begin()+i);
                 if(binary_search(nums.begin(), nums.end(), find))
                     return true;
        }
        return false;
    }
};