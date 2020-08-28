#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        self.arr = []
        def in_order(node):

            if node is None:
                return
            in_order(node.left)
            self.arr.append(node.val)
            in_order(node.right)

        in_order(root)

        result = float('inf')

        for i in range(len(self.arr)-1):

            temp = self.arr[i+1]-self.arr[i]
            result = temp if temp < result else result

        return result


# @lc code=end
