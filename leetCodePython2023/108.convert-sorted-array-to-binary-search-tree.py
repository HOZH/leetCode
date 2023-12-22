#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        length = len(nums)
        if length == 0:
            return None
        m = (length-1)//2
        left, right = nums[:m], nums[m+1:]

        root = TreeNode(nums[m])

        if len(left) > 0:
            root.left = self.sortedArrayToBST(left)
        if len(right) > 0:
            root.right = self.sortedArrayToBST(right)

        return root
