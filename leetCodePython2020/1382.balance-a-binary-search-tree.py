#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.ordered = []
        def in_order(node):

            if not node:
                return None

            in_order(node.left)
            self.ordered.append(node.val)
            in_order(node.right)

        in_order(root)

        def build_bst(start, end):

            if start > end:
                return None
            #
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.ordered = []
        def in_order(node):

            if not node:
                return None

            in_order(node.left)
            self.ordered.append(node.val)
            in_order(node.right)

        in_order(root)

        def build_bst(arr):

            if not len(arr):
                return None

            m = 0 + (len(arr) - 1) // 2

            current = TreeNode(arr[m])

            left = build_bst(arr[:m])
            right = build_bst(arr[m+1:])

            current.left = left
            current.right = right

            return current

        return build_bst(self.ordered)


# @lc code=end
