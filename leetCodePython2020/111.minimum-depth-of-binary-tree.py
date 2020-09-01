#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_d = self.minDepth(root.left)
        right_d = self.minDepth(root.right)
        if right_d == 0 and left_d == 0:
            return 1
        elif right_d == 0:
            return left_d+1
        elif left_d == 0:
            return right_d+1
        else:
            return min(left_d, right_d)+1
# @lc code=end
