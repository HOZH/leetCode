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

            # can add a determineter to end once the ans is found
            if node is None:
                return False, False

            left = helper(node.left)
            right = helper(node.right)

            is_p_included = True if (
                node == p or left[0] or right[0]) else False
            is_q_included = True if (
                node == q or left[1] or right[1]) else False

            if is_p_included and is_q_included:
                if self.ans is None:
                    self.ans = node

            return is_p_included, is_q_included

        helper(root)
        return self.ans


# @lc code=end
