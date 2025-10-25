#how to think: whenever we want to combine multiple lines of code into 1 line,
#think recursively -> recursion can help us save lots of lines of code

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        elements = []
        self.inorder(root, elements)
        return elements

    def inorder(self, root, elements):
        if root is not None:
            self.inorder(root.left, elements)
            elements.append(root.val)
            self.inorder(root.right, elements)
            return elements

