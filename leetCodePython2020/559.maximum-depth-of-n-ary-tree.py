#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
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
    def maxDepth(self, root: 'Node') -> int:

        if not root:
            return 0

        subs = []

        for child in root.children:

            subs.append(self.maxDepth(child))

        return max(subs)+1 if len(subs) else 1

# @lc code=end
