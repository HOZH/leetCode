#
# @lc app=leetcode id=1973 lang=python3
#
# [1973] Count Nodes Equal to Sum of Descendants
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(node):
            # current_sum
            current_sum = 0
            # left,right sum
            left_sum, right_sum = 0, 0
            if node.left:
                left_sum = helper(node.left)
            if node.right:
                right_sum = helper(node.right)
            self.ans += 1 if node.val == left_sum + right_sum else 0
            return node.val + left_sum + right_sum

        if not root:
            return 0

        helper(root)
        return self.ans
# @lc code=end
