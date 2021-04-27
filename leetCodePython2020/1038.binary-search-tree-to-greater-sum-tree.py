#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def helper(node, grant):

            if not node:
                return 0

            right = helper(node.right, grant)
            temp = node.val
            node.val += right+grant
            left = helper(node.left, node.val)

            return temp+left+right

        helper(root, 0)

        return root


# @lc code=end
