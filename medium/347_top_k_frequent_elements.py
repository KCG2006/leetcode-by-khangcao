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


# Time: O(N*logK)
# Space: O(N)
import heapq
from collections import Counter
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]


# Time: O(N)
# Space: O(N)
from collections import Counter
class Solution3(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        counter = Counter(nums)
        bucket = [0]*(n+1) #because the freq never go beyond n
        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]
            else:
                bucket[freq].append(num)
        ret = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                ret.extend(bucket[i])
            if len(ret) == k:
                return ret





