#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        self.nodes = []

        def helper(node):

            if node:
                self.nodes.append(node)

                helper(node.next)

        helper(head)

        return self.nodes[len(self.nodes)//2]


# @lc code=end
