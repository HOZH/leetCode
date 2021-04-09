#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root):

        self.arr = []

        def helper(node):
            if node:
                helper(node.left)
                self.arr.append(node.val)
                helper(node.right)
        # def helper(node):
        #     if node:
        #         yield from helper(node.left)
        #         yield node.val
        #         yield from helper(node.right)

        ans = current = TreeNode(None)
        # for v in helper(root):
        helper(root)
        for v in self.arr:

            current.right = TreeNode(v)
            current = current.right

        return ans.right

# @lc code=end
