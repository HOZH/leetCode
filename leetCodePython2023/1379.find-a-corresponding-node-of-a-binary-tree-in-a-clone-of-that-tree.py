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
        self.ans = None

        def helper(node):
            if not node or self.ans != None:
                return
            if node.val == target.val:
                self.ans = node
                return
            helper(node.left)
            helper(node.right)

        helper(cloned)
        return self.ans


# @lc code=end
