#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import math

class Solution:
    trzz = TreeNode(None)

    def helper(self, node, arr):

        index = math.floor(len(arr) / 2)

        if len(arr) == 0:
            return
        if node is not None:

            node.val = arr[index]

            left_half = arr[:index]
            right_half = arr[index+1:]

            if len(left_half) > 0:
                node.left = TreeNode(None)

                self.helper(node.left, left_half)

            if len(right_half) > 0:
                node.right = TreeNode(None)

                self.helper(node.right, right_half)

    def sortedArrayToBST(self, nums):

        if len(nums) == 0:

            self.trzz = None
            pass

        elif len(nums) == 1:

            self.trzz.val = nums[0]

        else:

            if len(nums) > 0:
                self.trzz.right = TreeNode(None)
                self.helper(self.trzz, nums)

        return self.trzz
