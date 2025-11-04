class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dct = {}
        for i in range(len(nums)):
            if nums[i] in dct:
                dct[nums[i]] += 1

            else:
                dct[nums[i]] = 1
            if dct[nums[i]] > (len(nums) // 2):
                return nums[i]