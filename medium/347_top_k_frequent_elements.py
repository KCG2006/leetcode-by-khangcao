# Time: O(N*logN)
# Space: O(N)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for i in range(k):
            sorted_count[i] = sorted_count[i][0]
        return sorted_count[:k]


