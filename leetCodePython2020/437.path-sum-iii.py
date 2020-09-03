#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
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
    def pathSum(self, root: TreeNode, sum: int) -> int:

        self.ans = 0
        self.sums = defaultdict(int)
        self.sums[0] = 1

        def helper(node, current):
            if not node:
                return

            current += node.val
            # seek if there is a prev state holds the redundant
            self.ans += self.sums[current-sum]
            # add current state to the map
            self.sums[current] += 1
            helper(node.left, current)
            helper(node.right, current)
            # trim the current state so nodes on
            # the other forks can't acces to it
            self.sums[current] -= 1
        helper(root, 0)
        return self.ans


# @lc code=end
