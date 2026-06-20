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
            # Early return if flag is already set to True
            if not node or self.ans is True:
                return
            if node.left is None and node.right is None:
                if node.val+current_val == targetSum:
                    self.ans = True
                return
            helper(node.left, current_val+node.val)
            helper(node.right, current_val+node.val)

        helper(root, 0)
        return self.ans

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False

        self.helper(root, 0, targetSum)

        return self.result

    def helper(self, root, accum, targetSum) -> None:
        if root is None or self.result is True:
            return
        total = accum + root.val
        if root.left is None and root.right is None:
            if total == targetSum:
                self.result = True 
                return

        if root.left is not None:
            self.helper(root.left, total, targetSum)
        if root.right is not None:
            self.helper(root.right, total, targetSum)
        return
        
# @lc code=end
