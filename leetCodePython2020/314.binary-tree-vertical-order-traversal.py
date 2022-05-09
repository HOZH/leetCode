#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ans = defaultdict(list)

        def helper(node, x_pos, y_pos):
            if not node:
                return

            ans[x_pos].append((node.val, y_pos))
            helper(node.left, x_pos-1, y_pos+1)
            helper(node.right, x_pos+1, y_pos+1)

        helper(root, 0, 0)

        orders = sorted(ans.keys())
        result = []
        for i in orders:
            temp = ans[i]
            temp.sort(key=lambda x: x[1])
            temp = list(map(lambda x: x[0], temp))
            result.append(temp)
        return result

# @lc code=end
