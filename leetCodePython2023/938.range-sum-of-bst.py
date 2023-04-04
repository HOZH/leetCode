#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0

        def helper(node):
            if not node:
                return
            if low <= node.val <= high:
                self.total += node.val
                helper(node.left)
                helper(node.right)

            if node.val < low:
                helper(node.right)
            if node.val > high:
                helper(node.left)

        helper(root)

        return self.total


# @lc code=end
