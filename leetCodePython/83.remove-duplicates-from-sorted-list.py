#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):

        current = head
        if current:

            prev = current

            while current:

                while current.next:

                    if current.next.val == current.val:
                        current = current.next
                    else:
                        break

                temp = current.next
                prev.next = temp
                prev = current = temp
                current = prev

        return head
