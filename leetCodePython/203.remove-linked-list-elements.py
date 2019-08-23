#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        current = head

        prev = None
        new_head = head

        while current:

            if current.val == val:

                if prev != None:

                    prev.next = current.next

                else:
                    new_head = current.next

            else:
                prev = current

            current = current.next

        return new_head
