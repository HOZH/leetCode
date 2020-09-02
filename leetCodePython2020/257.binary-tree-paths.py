#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        self.result = []

        def helper(node, string):
            if not node:
                return True

            left_none = helper(node.left, string+str(node.val)+'->')
            right_none = helper(node.right, string+str(node.val)+'->')

            if left_none and right_none:
                self.result.append(string+str(node.val))

            return False

        helper(root, '')
        return self.result


# @lc code=end
