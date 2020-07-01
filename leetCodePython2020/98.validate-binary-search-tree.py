#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def isValidBST_inorder(self, root: TreeNode) -> bool:

        self.arr = []

        def in_order(node):
            if node is None:
                return

            if node.left:
                in_order(node.left)

            self.arr.append(node.val)

            if node.right:
                in_order(node.right)

        in_order(root)
        print(self.arr)
        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True

    def helper(self, root, min_val, max_val):

        if root is None:
            return True

        if root.val <= min_val or root.val >= max_val:
            return False
        return self.helper(root.left, min_val, root.val) and self.helper(root.right, root.val, max_val)

    def isValidBST(self, root: TreeNode) -> bool:

        return self.helper(root, float('-inf'), float('inf'))


# @lc code=end
