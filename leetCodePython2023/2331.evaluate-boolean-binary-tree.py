#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if node.left is None and node.right is None:
                return True if node.val == 1 else False
            if node.val == 2:
                return helper(node.left) or helper(node.right)
            else:
                return helper(node.left) and helper(node.right)

        return helper(root)

# @lc code=end
