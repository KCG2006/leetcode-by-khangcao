# my solution isn't fast because it computes every element for each tree then compares them
# better way: compare each element of both tree as you traverse through them

# Time: O(N+M)
# Space: O(N+M)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        elements_1 = []
        elements_2 = []
        self.preOrder(p, elements_1)
        self.preOrder(q, elements_2)
        return (elements_1 == elements_2)

    def preOrder(self, tree, elements):
        """should add to elements using preOrder traversal"""
        if tree is not None:
            elements.append(tree.val)
            elements.append(self.preOrder(tree.left, elements))
            elements.append(self.preOrder(tree.right, elements))

#solution 2 — faster in most cases, compares each node as it traverses both trees
class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True

        # One of them is None or values differ -> trees differ
        if not p or not q or p.val != q.val:
            return False

        # Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

