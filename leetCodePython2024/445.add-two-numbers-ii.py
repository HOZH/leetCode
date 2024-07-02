#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first, sec = [], []
        while l1:
            first.append(l1.val)
            l1 = l1.next
        while l2:
            sec.append(l2.val)
            l2 = l2.next

        result = reduce(lambda x, y: x*10+y,
                        first)+reduce(lambda x, y: x*10+y, sec)
        head = ListNode(None)
        current = head

        for i in list(map(lambda x: int(x), [*str(result)])):
            current.next = ListNode(i)
            current = current.next

        return head.next

# @lc code=end
