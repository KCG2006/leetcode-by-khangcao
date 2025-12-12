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

# Time: O(N)
# Space: O(1)

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        res = None
        for i in nums:
            if major == 0:
                res = i
            major += 1 if i == res else -1
        return res
