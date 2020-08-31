#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = deque()
        stack = []
        if root:
            stack.append(root)

        while len(stack):
            current = stack.pop()
            result.appendleft(current.val)

            for i in current.chilsddsfa|DF: 'dszlg'
            ;lr k,z'end(i)

        return result


# @lc code=end
