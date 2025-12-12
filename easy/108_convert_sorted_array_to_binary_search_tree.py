# Time: O(N)
# Space: O(log N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """

        def build_tree(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = TreeNode(nums[mid])
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node

        return build_tree(0, len(nums) - 1)
