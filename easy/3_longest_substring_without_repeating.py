# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Tag: Hash Table, String, Sliding Window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = []
        max_list = []

        for c in s:
            if c in str_list:
                # Nếu c lặp lại, loại bỏ từng ký tự từ đầu str_list đến khi c không còn
                while c in str_list:
                    str_list.pop(0)
            str_list.append(c)

            if len(str_list) > len(max_list):
                max_list = str_list[:]

        return len(max_list)
