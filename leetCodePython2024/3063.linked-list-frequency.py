#
# @lc app=leetcode id=3063 lang=python3
#
# [3063] Linked List Frequency
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import defaultdict


class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        frequencies = defaultdict(int)
        while head:
            frequencies[head.val] += 1
            head = head.next

        prev = ListNode()
        current = prev
        for _, val in frequencies.items():
            current.next = ListNode(val)
            current = current.next

        return prev.next


# @lc code=end
