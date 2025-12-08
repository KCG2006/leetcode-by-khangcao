# Time: O(N*logN + M*logM)
# Space: O(N+M) for Python (Timsort)

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content_children = 0
        cookie_index = 0

        while cookie_index < len(s) and content_children < len(g):
            if g[content_children] <= s[cookie_index]:
                content_children += 1
            cookie_index += 1
        return content_children

