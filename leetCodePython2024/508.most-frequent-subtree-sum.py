#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
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
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.vals = []

        def helper(node):
            if not node:
                return

            temp = node.val+(helper(node.left) if node.left else 0) + \
                (helper(node.right) if node.right else 0)
            self.vals.append(temp)

            return temp

        helper(root)

        counter = Counter(self.vals)
        max_count = counter.most_common(1)[0][1]
        ans = []

        for key, val in counter.items():
            if val == max_count:
                ans.append(key)

        return ans
        
# @lc code=end

