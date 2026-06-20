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
from platform import node


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.values = []

        def in_order_traversal(node):
            if node is None:
                return

            in_order_traversal(node.left)
            self.values.append(node.val)
            in_order_traversal(node.right)

        in_order_traversal(root)
        # min_diff = float('inf')
        # for i in range(len(self.values)-1):
        #     current_val, next_val = self.values[i], self.values[i+1]
        #     min_diff = min(min_diff, abs(current_val-next_val))

        # a = [1, 2, 3]
        # b = [4, 5, 6, 7]
        # c = zip(a, b) = [(1, 4), (2, 5), (3, 6)]
        min_diff = min(y-x for x, y in zip(self.values, self.values[1:]))

        return min_diff
# @lc code=end


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # self.result = float('inf')
        # self.inOrder(root)
        # return self.result
        result = float('inf')
        diff = self.inOrder(root)
        return min(result, diff)

    def inOrder(self, root):
        if root is None:
            return None

        left = float('inf')
        if root.left is not None:
            left = self.inOrder(root.left)  # at 1, 0, #2 -> 1
        right = float('inf')
        if root.right is not None:
            right = self.inOrder(root.right)  # at 1, 0, 3

        left_diff = float('inf')
        right_diff = float('inf')
        if left is not None:
            left_diff = abs(left - root.val)  # 1, 3,
        if right is not None:
            right_diff = abs(root.val - right)  # 1, 3
        # self.result = min(self.result, left_diff, right_diff)
        # return min(left_diff if left_diff is not None else float('inf'), right_diff if right_diff is not None else float('inf'))
        # we should return node.val of the current node, also the min diff in the subtree(including current node) of current node
        return (root.val, min(left_diff, right_diff, min_diff_carried_from_left_subtree, min_diff_carried_from_right_subtree))
        # return min(left_diff, right_diff)

 5
/
1
