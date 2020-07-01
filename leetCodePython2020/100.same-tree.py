#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if p is None or q is None:
            return p == q

        if p.val != q.val:
            return False

        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# @lc code=end
