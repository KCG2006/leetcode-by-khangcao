# https://leetcode.com/problems/two-sum/
# difficulty: Easy
# Tag: Hash Table, Array
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #create a dict to store number that is not in the dict
        num_dict = {}
        for i in range(len(nums)):
            #check if complement is in dict
            if (target - nums[i]) in num_dict:
                # return the index of those two
                return [num_dict[(target - nums[i])], i]
            else: #store that num and its index to the dict
                num_dict[nums[i]] = i
