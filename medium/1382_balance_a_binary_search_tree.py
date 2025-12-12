# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def balanceBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def in_order_traversal(root):
            if root.left:
                in_order_traversal(root.left)
            elements.append(root)
            if root.right:
                in_order_traversal(root.right)
        def build_tree(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            node = elements[mid]
            node.left = build_tree(left, mid - 1)
            node.right = build_tree(mid + 1, right)
            return node
        elements = []
        in_order_traversal(root)
        return build_tree(0, len(elements) - 1)




