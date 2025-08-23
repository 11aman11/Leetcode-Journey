// Last updated: 8/23/2025, 3:51:52 PM
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int sum;
        vector<int> vect;
        for(int i=0;i<nums.size();i++)
        {
            if(i==nums.size()-1)
                break;
            for(int j=i+1;j<nums.size();j++)
            {
                sum=nums[i]+nums[j];
                if(sum==target)
                {
                    vect.push_back(i);
                    vect.push_back(j);
                    break;
                }
            }
        }   
        return vect;
    }
};