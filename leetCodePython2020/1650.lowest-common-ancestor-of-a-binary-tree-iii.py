#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # p_current, q_current = p, q
        # p_pattern, q_pattern = [], []
        # while p_current:
        #     p_pattern.append(p_current)
        #     p_current = p_current.parent
        # while q_current:
        #     q_pattern.append(q_current)
        #     q_current = q_current.parent

        # placeholder = set(q_pattern)&set(p_pattern)

        # return min(placeholder, key = lambda x:p_pattern.index(x))
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p

        return p1

# @lc code=end
