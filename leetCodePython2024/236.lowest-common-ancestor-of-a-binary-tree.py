#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None

        def helper(node):
            if not node:
                return False, False

            left, right = helper(node.left), helper(
                node.right)

            child_p_found = left[0] or right[0]
            child_q_found = left[1] or right[1]
            if (child_p_found or node.val == p.val) and (child_q_found or node.val == q.val):
                if self.ans is None:
                    self.ans = node
                return True, True

            return (child_p_found or node.val == p.val), (child_q_found or node.val == q.val)

        helper(root)
        return self.ans

# @lc code=end
