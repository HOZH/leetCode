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

        if not head or not head.next:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow is fast:
                while slow is not head:
                    slow, head = slow.next, head.next
                return slow

        return None
# @lc code=end
