#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        self.result = []

        def helper(node, target, arr):

            if not node:
                return

            new_arr = arr+[node.val]

            if node.val == target:

                if not node.left and not node.right:
                    self.result.append(new_arr)
                    return

            helper(node.left, target-node.val, new_arr[:])
            helper(node.right, target-node.val, new_arr[:])

        helper(root, sum, [])
        return self.result


# @lc code=end
