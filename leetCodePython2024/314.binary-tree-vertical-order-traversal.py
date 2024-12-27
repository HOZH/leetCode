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
from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.cols = defaultdict(list)

        queue = deque([(root, 0)])
        while len(queue):
            current_layer_len = len(queue)
            while current_layer_len > 0:
                node, index = queue.popleft()
                self.cols[index].append(node.val)
                if node.left:
                    queue.append((node.left, index-1))
                if node.right:
                    queue.append((node.right, index+1))
                current_layer_len -= 1

        # def helper(node, index):
        #     if not node:
        #         return
        #     helper(node.left, index-1)
        #     helper(node.right, index+1)
        #     self.cols[index].append(node.val)

        # helper(root, 0)
        list_items = sorted(self.cols.items(), key=lambda x: x[0])
        return list(map(lambda x: x[1], list_items))

# @lc code=end
