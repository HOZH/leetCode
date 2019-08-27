#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.ans = 0

        def helper(node):

            if not node:
                return 0

            left_length = helper(node.left)
            right_length = helper(node.right)

            left = right = 0

            if node.left and node.left.val == node.val:

                left = left_length+1

            if node.right and node.right.val == node.val:

                right = right_length+1

            self.ans = max(self.ans, left+right)

            return max(left, right)

        helper(root)

        return self.ans
