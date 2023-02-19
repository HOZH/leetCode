#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.ans = 0

        def helper(node):
            if not node:
                return 0, 0

            left, right = helper(node.left), helper(node.right)
            sub_tree_sum = (node.val+left[0]+right[0])
            sub_tree_count = (1+left[1]+right[1])
            if node.val == sub_tree_sum//sub_tree_count:
                self.ans += 1
            return sub_tree_sum, sub_tree_count

        helper(root)
        return self.ans


# @lc code=end
