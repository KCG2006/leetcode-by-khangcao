# Time: O(N)
# Space: O(N)

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_table_1 = {}
        hash_table_2 = {}
        for i in range(len(s)):
            if hash_table_1.get(s[i], -1) != hash_table_2.get(t[i], -1):
                return False
            if s[i] not in hash_table_1 and t[i] not in hash_table_2:
                hash_table_1[s[i]] = len(hash_table_1)
                hash_table_2[t[i]] = len(hash_table_2)
        return True

