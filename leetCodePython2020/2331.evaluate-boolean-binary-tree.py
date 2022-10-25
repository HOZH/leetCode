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
            value = node.val
            if value == 0:
                return False
            elif value == 1:
                return True
            else:
                left, right = helper(node.left), helper(node.right)
                if value == 2:
                    return left or right
                else:
                    return left and right

        return helper(root)
# @lc code=end
