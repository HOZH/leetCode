#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def helper(node, s):

            temp = s

            if node:

                value = node.val

                temp -= value

                left = helper(node.left, temp)
                right = helper(node.right, temp)

                if value == s:

                    if left is None and right is None:
                        return True

                if left:
                    return left

                elif right:
                    return right
                else:
                    return False

        return helper(root, sum)
