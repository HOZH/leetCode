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
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0

        def traverse_tree(node):
            if not node:
                return (0, 0)
            left_sum, left_count = traverse_tree(node.left)
            right_sum, right_count = traverse_tree(node.right)
            if not left_count and not right_count:
                self.ans += 1
                return (node.val, 1)
            else:
                total_sum = left_sum + right_sum + node.val
                total_count = left_count + right_count + 1
                if total_sum // total_count == node.val:
                    self.ans += 1
                return (total_sum, total_count)
        traverse_tree(root)
        return self.ans


# @lc code=end
