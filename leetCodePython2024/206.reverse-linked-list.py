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
    # def __init__(self) -> None:
    #     self.ans = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next =head
        head.next = None
        return p

        # def helper(node):
        #     if not node:
        #         return None

        #     temp = helper(node.next)
        #     if not temp:
        #         self.ans = node
        #         return node

        #     temp.next = node
        #     node.next = None
        #     return node

        # helper(head)
        # return self.ans

# @lc code=end
