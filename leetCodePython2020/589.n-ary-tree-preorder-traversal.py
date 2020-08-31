#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        stack = []
        if root:
            stack.append(root)

        # FILO stack
        while len(stack):
            current = stack.pop()
            self.result.append(current.val)

            for i in current.children[::-1]:
                stack.append(i)

        return self.result

# @lc code=end
