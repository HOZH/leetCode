#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.arr.append(node.val)
            in_order(node.right)

        in_order(root)
        counter = Counter(self.arr)
        ans = []
        max_count = counter.most_common(1)[0][1]
        for i, j in counter.items():
            if j == max_count:
                ans.append(i)

        return ans


# @lc code=end
