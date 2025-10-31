# Time: O(log N)
# Space: O(log N)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(left, right):
            if left > right:
                return left
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            elif nums[mid] < target:
                return binary_search(mid + 1, right)

        return binary_search(0, len(nums) - 1)


