#
# @lc app=leetcode id=1676 lang=python3
#
# [1676] Lowest Common Ancestor of a Binary Tree IV
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        node_vals = set()
        for i in nodes:
            node_vals.add(i.val)
        ans = len(node_vals)
        self.result = None

        def helper(node):
            if not node:
                return None, 0

            node.left, left_count = helper(node.left)
            node.right, right_count = helper(node.right)
            count = left_count+right_count

            if node.val in node_vals:
                count += 1
            if count == ans:
                if self.result is None:
                    self.result = node

            return node, count

        helper(root)
        return self.result


# @lc code=end
