#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            helper(node.right)
            self.ans.append(node.val)

        helper(root)
        return self.ans
        
# @lc code=end

