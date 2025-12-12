# Time: O(N)
# Space: O(N)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        dct = {}
        while curr is not None:
            if curr not in dct:
                dct[curr] = curr.next
                curr = curr.next
            else:
                return True
        return False

# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        curr1 = head
        curr2 = head
        while curr1 and curr1.next:
            curr1 = curr1.next.next
            curr2 = curr2.next
            if curr1 == curr2:
                return True
        return False

