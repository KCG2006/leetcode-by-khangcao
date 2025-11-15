# Time: O(N)
# Space: O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True
        def is_symmetric(left_child, right_child):
            if not left_child and not right_child:
                return True
            if not left_child or not right_child:
                return False
            if left_child.val != right_child.val:
                return False
            else:
                return is_symmetric(left_child.left, right_child.right) and is_symmetric(left_child.right,
                                                                                         right_child.left)
        return is_symmetric(root.left, root.right)


# Time: O(N)
# Space: O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True

        q = deque()
        q.append((root.left, root.right))

        while q:
            left, right = q.popleft()
            if not left and not right:
                continue
            if (not left and right) or (left and not right):
                return False
            if left.val != right.val:
                return False
            else:
                q.append((left.left, right.right))
                q.append((left.right, right.left))
        return True