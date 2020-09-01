#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        self.arr1 = []
        self.arr2 = []

        def helper(node, arr):

            if not node:
                return True

            left_none = helper(node.left, arr)
            right_none = helper(node.right, arr)

            if left_none and right_none:
                arr.append(node.val)

            return False

        helper(root1, self.arr1)
        helper(root2, self.arr2)

        return self.arr1 == self.arr2


# @lc code=end
