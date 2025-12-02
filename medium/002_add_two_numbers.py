# Time: O(Max(N,M))
# Space: O(Max(N,M))

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        c1 = l1
        c2 = l2
        prev = None
        carry = 0

        while c1 or c2:
            v1 = c1.val if c1 else 0
            v2 = c2.val if c2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            digits = total - carry * 10

            if c1:
                c1.val = digits
                prev = c1
                c1 = c1.next
            else:
                prev.next = ListNode(digits)
                prev = prev.next
            if c2:
                c2 = c2.next
        if carry:
            prev.next = ListNode(carry)
        return l1


