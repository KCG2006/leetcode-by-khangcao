# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        ans = ListNode(-1, head)
        curr = ans
        while curr:
            while curr.next and curr.next.val == val:
                curr.next = curr.next.next
            curr = curr.next
        return ans.next






