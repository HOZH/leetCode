#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def helper(self, node, string):

        if node:

            string += "->"+str(node.val)

            if not node.left and not node.right:

                self.answer.append(string)

            elif node.left and node.right:

                self.helper(node.left, string)
                self.helper(node.right, string)

            elif node.right:

                self.helper(node.right, string)

            else:

                self.helper(node.left, string)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        self.answer = list()

        if root:

            temp_string = str(root.val)
            if not root.left and not root.right:

                self.answer.append(temp_string)
            else:

                self.helper(root.left, temp_string)
                self.helper(root.right, temp_string)

            return self.answer

        else:

            return""
