#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
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
    def minDepth(self, root: TreeNode) -> int:
        # bfs
        if not root:
            return 0

        queue = deque([root])

        depth = 0

        while queue:

            current_level_count = len(queue)

            depth += 1

            while current_level_count:
                current = queue.pop()
                current_level_count -= 1
                if not current.left and not current.right:
                    return depth
                else:
                    if current.left:
                        queue.appendleft(current.left)
                    if current.right:
                        queue.appendleft(current.right)

        return depth

    def minDepth_dfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_d = self.minDepth(root.left)
        right_d = self.minDepth(root.right)

        if right_d == 0:
            return left_d+1
        elif left_d == 0:
            return right_d+1
        else:
            return min(left_d, right_d)+1
# @lc code=end
