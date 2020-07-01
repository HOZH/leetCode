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

        if len(nums) == 0:
            return None

        mid = (len(nums)-1)//2
        left_n = nums[:mid]
        right_n = nums[mid+1:]
        root = TreeNode(nums[mid])

        if len(left_n) != 0:
            root.left = self.sortedArrayToBST(left_n)

        if len(right_n) != 0:

            root.right = self.sortedArrayToBST(right_n)

        return root


# @lc code=end
