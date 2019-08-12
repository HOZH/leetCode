#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, node, length):

        if node:

            left = self.helper(node.left, length+1)
            right = self.helper(node.right, length+1)

            local_left = left-length
            local_right = right-length

            if left + right == 0:
                single = length

            else:
                single = left if left > right else right

            c = local_left+local_right

            if self.total < c:
                self.total = c


            return single
        else:

            return 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.total = 0

        if root:

            self.helper(root, 0)

            return self.total

        else:
            return 0
