#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        self.arr = []

        def preorder(node):
            if not node:
                return

            self.arr.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return all(list(map(lambda x: x == self.arr[0], self.arr)))

# @lc code=end
