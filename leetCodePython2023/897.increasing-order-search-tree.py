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
    def increasingBST(self, root: TreeNode) -> TreeNode:

        self.vals = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            self.vals.append(node.val)
            helper(node.right)

        helper(root)

        if not len(self.vals):
            return None

        head = TreeNode(self.vals[0])
        self.vals = self.vals[1:]

        def create_tree(node):
            if len(self.vals):
                node.right = TreeNode(self.vals[0])
                self.vals = self.vals[1:]
                create_tree(node.right)

            return node

        create_tree(head)
        return head


# @lc code=end
