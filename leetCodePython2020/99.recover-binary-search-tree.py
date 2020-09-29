#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def recoverTree(self, root: TreeNode) -> None:

        self.prev = None
        self.first, self.sec = None, None

        def in_order(node):
            if node is None:
                return

            in_order(node.left)
            if self.prev is not None and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev

                self.second = node

            self.prev = node

            in_order(node.right)

        in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def recoverTree_in_place(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.arr = []

        def in_order(node):
            if node is None:
                self.arr.append(None)

            if node.left:
                in_order(node.left)

            self.arr.append(node.val)

            if node.right:
                in_order(node.right)

        in_order(root)

        self.arr.sort()

        def in_order_fix(node):
            if node is None:
                return

            if node.left:
                in_order_fix(node.left)

            node.val = self.arr[0]
            self.arr = self.arr[1:]

            if node.right:
                in_order_fix(node.right)

        in_order_fix(root)


# @lc code=end
