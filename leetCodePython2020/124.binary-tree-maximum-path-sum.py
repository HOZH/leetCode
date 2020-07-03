#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def helper(node, max_val):

            if node is None:
                return 0

            left = max(0, helper(node.left, max_val))
            right = max(0, helper(node.right, max_val))

            local_max = node.val+max(left, right)
            temp = node.val + left + right
            if temp > max_val[0]:
                max_val[0] = temp

            return local_max

        self.max_val = [float('-inf')]
        helper(root, self.max_val)

        return self.max_val[0]

# @lc code=end
