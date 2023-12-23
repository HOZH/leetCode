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
        if not root:
            return 0

        self.ans = 0

        def helper(node, val):
            current_val = val*10+node.val

            if not node.left and not node.right:
                self.ans += current_val
            else:
                if node.left:
                    helper(node.left, current_val)
                if node.right:
                    helper(node.right, current_val)

        helper(root, 0)
        return self.ans


# @lc code=end
