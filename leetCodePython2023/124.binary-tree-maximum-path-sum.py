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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def helper(node):
            if not node:
                return 0
            left_sum, right_sum = helper(node.left), helper(node.right)

            one_way_root_max = node.val+max(left_sum, right_sum, 0)
            two_way_root_max = max(left_sum+right_sum, 0)+node.val
            self.max_sum = max(
                self.max_sum, one_way_root_max, two_way_root_max)

            return one_way_root_max

        helper(root)
        return self.max_sum

# @lc code=end
