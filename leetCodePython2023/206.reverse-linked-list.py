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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, current = None, head

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev

        # if head is None:
        #     return None

        # self.answer = None

        # def helper(node):
        #     if node.next:
        #         temp = helper(node.next)
        #         temp.next = node
        #         node.next = None
        #     else:
        #         self.answer = node

        #     return node
        
        # helper(head)

        # return self.answer

        
# @lc code=end

