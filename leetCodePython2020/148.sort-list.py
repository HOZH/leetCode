#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # merge sort, heap sort will do in nlogn time,
        # or even quick sort will do in expected nlogn time

        current = head
        temp = []
        while current is not None:
            temp.append(current.val)
            current = current.next

        temp.sort()
        current = head
        for i in temp:
            current.val = i
            current = current.next

        return head


# @lc code=end
