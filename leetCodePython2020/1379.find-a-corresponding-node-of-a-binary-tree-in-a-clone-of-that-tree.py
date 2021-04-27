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

        self.ori, self.copied = [], []

        def in_order(node, container):

            if not node:
                return

            in_order(node.left, container)
            container.append(node)
            in_order(node.right, container)

        in_order(original, self.ori)
        in_order(cloned, self.copied)

        index = -1
        for i in range(len(self.ori)):
            if self.ori[i].val == target.val:
                index = i
                break

        return self.copied[index]


# @lc code=end
