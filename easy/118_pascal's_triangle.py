# Time: O(N^2)
# Space: O(N^2)

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        ret = [[1]]
        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                val = ret[i - 1][j - 1] + ret[i - 1][j]
                row.append(val)
            row.append(1)
            ret.append(row)
        return ret

