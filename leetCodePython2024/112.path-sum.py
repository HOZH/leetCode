#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = False

        def helper(node, current_val):
            if not node:
                return
            if node.left is None and node.right is None:
                if node.val+current_val == targetSum:
                    self.ans = True
            else:
                helper(node.left, current_val+node.val)
                helper(node.right, current_val+node.val)

        helper(root, 0)
        return self.ans


# @lc code=end
