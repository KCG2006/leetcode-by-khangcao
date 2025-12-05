# Time: O(4^N/(N^(1/2))
# Space: O(4^N/(N^(1/2))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        if n == 0:
            return []

        def build(left, right):
            if left > right:
                return [None]
            all_trees = []
            for i in range(left, right + 1):
                left_subtrees = build(left, i - 1)
                right_subtrees = build(i + 1, right)

                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root = TreeNode(i)
                        root.left = left_subtree
                        root.right = right_subtree
                        all_trees.append(root)
            return all_trees

        return build(1, n)


