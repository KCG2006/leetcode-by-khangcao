# Time: O(N)
# Space: O(1)

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[count] = nums[i]
                count += 1
        return len(nums[:count])
