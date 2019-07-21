#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findTarget(self, root: TreeNode, k: int) -> bool:

        ss = set()

        def solve(rt, k, ss):

            if k - rt.val in ss:
                return True
            ss.add(rt.val)

            return (solve(rt.left, k, ss) if rt.left else False) or(solve(rt.right, k, ss) if rt.right else False)
        return solve(root, k, ss)
