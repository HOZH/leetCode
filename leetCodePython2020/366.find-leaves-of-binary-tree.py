#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.bag = defaultdict(list)

        def helper(node):
            if not node:
                return -1
            left = helper(node.left)
            right = helper(node.right)
            temp = max(left, right)+1
            self.bag[temp].append(node.val)
            return temp
        helper(root)
        ans = []
        for i in sorted(self.bag.keys()):
            ans.append(self.bag[i])
        return ans


# @lc code=end
