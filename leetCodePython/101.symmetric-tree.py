#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, node, lis, left):

        if not node:

            lis.append(None)

        else:

            lis.append(node.val)

            if left:

                lis = self.helper(node.right, self.helper(
                    node.left, lis, True), True)

            else:

                lis = self.helper(node.left, self.helper(
                    node.right, lis, False), False)

        return lis

    def isSymmetric(self, root: TreeNode) -> bool:

        if root:

            left = self.helper(root.left, list(), True)
            right = self.helper(root.right, list(), False)

            return left == right

        return True
