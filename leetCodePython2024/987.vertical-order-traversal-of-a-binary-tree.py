#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vals = []

        def preorder(x, y, node):
            if not node:
                return
            vals.append((x, y, node.val))
            preorder(x-1, y+1, node.left)
            preorder(x+1, y+1, node.right)

        preorder(0, 0, root)

        ans = []

        last_x = float('-inf')
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)

        return ans

# @lc code=end

