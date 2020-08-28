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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def ll_2_num(l):
            result = 0
            while l:
                result *= 10
                result += l.val
                l = l.next
            return result

        temp = str(ll_2_num(l1)+ll_2_num(l2))

        head = ListNode()
        current = head
        while len(temp):

            current.next = ListNode(int(temp[0]))
            current = current.next
            temp = temp[1:]

        return head.next

# @lc code=end
