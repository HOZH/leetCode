#
# @lc app=leetcode id=1265 lang=python3
#
# [1265] Print Immutable Linked List in Reverse
#

# @lc code=start
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        if not head:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()

# @lc code=end
