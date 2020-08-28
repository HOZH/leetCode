#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        first, sec = l1, l2
        result = ListNode()
        current = result

        while first or sec:
            f, s = first.val if first else None, sec.val if sec else None

            if f is None:
                current.next = sec
                sec = None

            elif s is None:
                current.next = first
                first = None

            else:
                if f > s:
                    current.next = sec
                    sec = sec.next
                else:
                    current.next = first
                    first = first.next

            current = current.next

        return result.next

# @lc code=end
