#
# @lc app=leetcode id=1522 lang=python3
#
# [1522] Diameter of N-Ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.diameter_value = 0

        def helper(node):
            if not node:
                return 0
            children_depths = []
            for child in node.children:
                depth = helper(child)
                children_depths.append(depth)
            sorted_children_depths = sorted(children_depths, reverse=True)
            max_root_depth = sum(sorted_children_depths[:2])
            self.diameter_value = max(
                self.diameter_value, max_root_depth)

            return max(sorted_children_depths+[0])+1

        helper(root)
        return self.diameter_value
# @lc code=end
