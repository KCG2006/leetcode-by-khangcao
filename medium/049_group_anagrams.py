# Time: O(Nk*logk)
# Space: O(Nk)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        ret = defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            ret[key].append(s)
        return list(ret.values())
