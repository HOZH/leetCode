#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def rec_helper(self, node):

        if node.next is None:

            self.head = node
            return node

        else:
            old_next = node.next
            node.next = None
            temp = self.rec_helper(old_next)
            temp.next = node

            return node

    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        current, prev = head, None

        while current.next:

            temp_next = current.next
            temp = temp_next.next
            current.next = prev

            temp_next.next = current
            prev = temp_next
            if temp is None:
                prev = current
                current = temp_next

                break
            current = temp

        current.next = prev

        return current

        # self.rec_helper(head)

        # return self.head

# @lc code=end
