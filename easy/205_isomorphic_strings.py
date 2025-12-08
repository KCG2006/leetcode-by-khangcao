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

# Time: O(N)
# Space: O(N)

class Solution2(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        mapping_s_t = {}
        mapped_t = set()
        for cs, ct in zip(s, t):
            if cs in mapping_s_t:
                if mapping_s_t[cs] != ct:
                    return False
            else:
                if ct in mapped_t:
                    return False
                mapping_s_t[cs] = ct
                mapped_t.add(ct)
        return True



