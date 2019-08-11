#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, node, level):

        if node:

            length = len(self.answers)

            if level >= length:

                self.answers.insert(level, [node.val])

            else:

                self.answers[level].append(node.val)

            self.helper(node.left, level+1)
            self.helper(node.right, level+1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        self.answers = list()

        self.helper(root, 0)

        return self.answers[::-1]
