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

    def reverseList(self, head: ListNode) -> ListNode:

        self.first = None

        def helper(node):
            if node is None:
                return None
            temp_next = node.next
            node.next = None
            temp = helper(temp_next)
            if temp:
                temp.next = node
            else:
                self.first = node
            return node

        helper(head)
        return self.first


# @lc code=end
