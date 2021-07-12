#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while len(queue):
            level_len = len(queue)
            current_level = []

            while level_len:
                current = queue.popleft()
                level_len -= 1
                queue.extend(current.children)

                current_level.append(current.val)
            result.append(current_level)

        return result
    # using bfs

    def levelOrder_temp(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = deque()
        if root:
            queue.append(root)

        while len(queue):
            level_len = len(queue)
            current_level = []

            while level_len:
                current = queue.popleft()
                level_len -= 1
                for i in current.children:
                    if i:
                        queue.append(i)
                current_level.append(current.val)
            result.append(current_level)

        return result


# @lc code=end
