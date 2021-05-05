#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        sec_tail = list2

        while sec_tail.next:
            sec_tail = sec_tail.next

        a_tail, b_head = None, None

        current = list1
        count = 0

        while current.next:

            if count == a-1:
                a_tail = current

            count += 1

            current = current.next

            if count == b+1:
                b_head = current

            if a_tail and b_head:
                break

        a_tail.next = list2
        sec_tail.next = b_head

        return list1


# @lc code=end
