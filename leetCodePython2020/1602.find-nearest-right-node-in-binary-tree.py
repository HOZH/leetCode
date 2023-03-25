#
# @lc app=leetcode id=1602 lang=python3
#
# [1602] Find Nearest Right Node in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        layers = []
        bag = deque([root])
        target_layer = -1

        while len(bag) > 0:
            current_layer_len = len(bag)
            temp_liz = []
            while current_layer_len > 0:
                current_layer_len -= 1
                current = bag.popleft()
                if current.val == u.val:
                    target_layer = len(layers)
                temp_liz.append(current)
                if current.left:
                    bag.append(current.left)
                if current.right:
                    bag.append(current.right)
            layers.append(temp_liz)

        temp = layers[target_layer]
        for i in range(len(temp)):
            if temp[i] == u:
                if i != len(temp)-1:
                    return temp[i+1]
                else:
                    return None

        return None


# @lc code=end
