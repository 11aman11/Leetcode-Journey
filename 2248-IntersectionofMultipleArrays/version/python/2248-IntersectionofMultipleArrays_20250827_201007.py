# Last updated: 8/27/2025, 8:10:07 PM
# say like this: we can build a frequency map using hashmap to store the frequency of each number across all sub arrays. then, each time a element appears in every sub-array, we increase its count. after building the frequency map,  we check if the count of each element is equal to length of nums which means that element appeared in all sub arrays within the array thus append it to output array and sort the output array for the result. words: frequency map, build, sub-arrays, result.
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # counts = defaultdict(int)
        # for arr in nums:
        #     for i in range(len(arr)):
        #         counts[arr[i]] += 1
        
        # out = []
        
        # for key in counts.keys():
        #     if counts[key] == len(nums):
        #         out.append(key)
        # return sorted(out)

        count = defaultdict(int)
        out = []
        

        for arr in nums:
            for item in arr:
                count[item] += 1
        
        for key in count:
            if count[key] == len(nums):
                out.append(key)
        return sorted(out)        

            


        













