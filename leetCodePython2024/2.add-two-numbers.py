#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from functools import reduce


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, sec, carry = 0, 0, 0
        head = ListNode(None)
        current = head
        while l1 is not None or l2 is not None or carry != 0:
            current_val = (l1.val if l1 is not None else 0) + \
                (l2.val if l2 is not None else 0) + carry
            if current_val > 9:
                carry = 1
                current_val -= 10
            else:
                carry = 0
            current.next = ListNode(current_val)
            current = current.next
            l1, l2 = l1.next if l1 is not None else None, l2.next if l2 is not None else None

        return head.next

        first, sec = [], []
        while l1:
            first.append(l1.val)
            l1 = l1.next
        while l2:
            sec.append(l2.val)
            l2 = l2.next

        result = reduce(lambda x, y: x*10+y,
                        first[::-1])+reduce(lambda x, y: x*10+y, sec[::-1])
        head = ListNode(None)
        current = head

        for i in list(map(lambda x: int(x), [*str(result)][::-1])):
            current.next = ListNode(i)
            current = current.next

        return head.next


# @lc code=end
