#
# @lc app=leetcode id=3263 lang=python3
#
# [3263] Convert Doubly Linked List to Array I
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""


class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        ans = []
        while root:
            ans.append(root.val)
            root = root.next

        return ans

# @lc code=end
