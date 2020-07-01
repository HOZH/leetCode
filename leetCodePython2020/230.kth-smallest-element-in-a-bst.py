#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = 0
        self.result = 0
        # may add a flag to demtermine when to stop to reach O(klogn) instead of O(nlogn)

        def in_order(node):
            if node is None:
                return

            if node.left:
                in_order(node.left)

            self.k += 1
            if self.k == k:
                self.result = node.val
                return

            if node.right:
                in_order(node.right)

        in_order(root)
        return self.result


# @lc code=end
