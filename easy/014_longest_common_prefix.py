# Time: O(N*M)
# Space: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for e in range(1, len(strs)):
            while strs[0] != strs[e][:len(strs[0])]:
                strs[0] = strs[0][:-1]
        return strs[0]