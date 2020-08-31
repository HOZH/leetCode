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
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0

        def helper(node, s, ans):
            if node is None:
                return
            s = s*10+node.val
            if node.left is None and node.right is None:
                self.ans += s
                return

            helper(node.left, s, ans)
            helper(node.right, s, ans)

        helper(root, 0, self.ans)
        return self.ans


# @lc code=end
