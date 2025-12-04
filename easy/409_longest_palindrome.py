# Time: O(N)
# Space: O(N)

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        dict_s = {}
        odd_found = False
        for i in range(len(s)):
            dict_s[s[i]] = dict_s.get(s[i], 0)+1

        for value in dict_s.values():
            if value % 2 == 0: #even
                count += value
            else:
                count += value -1
                odd_found = True

        if odd_found:
            count += 1
        return count