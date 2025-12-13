# Time: O(N)
# Space: O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        L = 0
        R = n-1

        while L<R:
            if not s[L].isalnum():
                L+=1
                continue
            if not s[R].isalnum():
                R-=1
                continue
            if s[L].lower() != s[R].lower():
                return False
            L+=1
            R-=1
        return True