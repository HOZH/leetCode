#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    left_total = 0

    def helper(self, node, left):

        if node:

            if left:

                if node.left is None and node.right is None:

                    self.left_total += node.val
                    return

            self.helper(node.left, True)
            self.helper(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        self.helper(root, False)

        return self.left_total
