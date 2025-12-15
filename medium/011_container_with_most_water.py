# Time: O(N)
# Space: O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        L = 0
        R = n-1
        max_area = 0
        while L < R:
            area = min(height[L], height[R])*(R-L)
            if area > max_area:
                max_area = area
            if height[L] <= height[R]:
                L+=1
            else:
                R-=1
        return max_area


