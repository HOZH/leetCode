#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # s = set()
        # while head:
        #     if head in s:
        #         return head
        #     s.add(head)
        #     head = head.next

        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow is fast:
                slow = head
                while slow is not fast:
                    slow, fast = slow.next, fast.next

                return fast

        return None
# @lc code=end
