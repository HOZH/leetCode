#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def helper(node, current_val):
            if not node:
                return
            temp = current_val*10+node.val

            if not node.left and not node.right:
                self.ans += temp
                return

            helper(node.left, temp)
            helper(node.right, temp)

        helper(root, 0)
        return self.ans


# @lc code=end
