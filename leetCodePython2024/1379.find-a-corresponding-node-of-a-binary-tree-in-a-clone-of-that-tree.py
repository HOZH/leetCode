#
# @lc app=leetcode id=1379 lang=python3
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ans = 0

        def helper(ori_node, clone_node):
            if not ori_node:
                return
            if ori_node.val == target.val:
                self.ans = clone_node
                return
            helper(ori_node.left, clone_node.left)
            helper(ori_node.right, clone_node.right)

        helper(original, cloned)
        return self.ans


# @lc code=end
