#
# @lc app=leetcode id=1490 lang=python3
#
# [1490] Clone N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        def helper(node):

            if not node:
                return None

            children = []
            for i in node.children:
                children.append(helper(i))

            temp = Node(node.val, children)
            return temp

        return helper(root)
# @lc code=end
