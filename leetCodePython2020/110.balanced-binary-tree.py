#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def helper(node):
            if not node:
                return 0
            left_d = helper(node.left)
            right_d = helper(node.right)
            if left_d == -1 or right_d == -1:
                return -1
            if abs(left_d-right_d) > 1:
                return -1
            return max(left_d, right_d)+1

        return True if helper(root) != -1 else False

# @lc code=end
