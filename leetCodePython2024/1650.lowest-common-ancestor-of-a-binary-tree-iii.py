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
from collections import OrderedDict


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # p_hierarchy = OrderedDict()
        # q_hierarchy = OrderedDict()
        # node = p
        # while node:
        #     p_hierarchy[node.val] = node
        #     node = node.parent
        # node = q
        # while node:
        #     q_hierarchy[node.val] = node
        #     node = node.parent

        # if p.val in q_hierarchy:
        #     return p
        # if q.val in p_hierarchy:
        #     return q
        # for key, val in p_hierarchy.items():
        #     if key in q_hierarchy:
        #         return val
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1


# @lc code=end
