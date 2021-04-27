#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return None
        current_index = nums.index(max(nums))

        node = TreeNode(nums[current_index])

        node.left = self.constructMaximumBinaryTree(nums[:current_index])
        node.right = self.constructMaximumBinaryTree(nums[current_index+1:])

        return node

# @lc code=end
