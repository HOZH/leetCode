#
# @lc app=leetcode id=2181 lang=python3
#
# [2181] Merge Nodes in Between Zeros
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = 0
        result = ListNode()
        pre_node = result
        while head.next != None:
            head = head.next
            if head.val != 0:
                current += head.val
            else:
                result.next = ListNode(current)
                current = 0
                result = result.next
        return pre_node.next if pre_node.next != None else pre_node


# @lc code=end
