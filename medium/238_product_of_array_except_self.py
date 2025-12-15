# Time: O(N)
# Space: O(1)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = 1
        postfix = 1
        answer = [1] * n
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            answer[i + 1] *= prefix
        for i in range(len(nums) - 1, 0, -1):
            postfix *= nums[i]
            answer[i - 1] *= postfix
        return answer
