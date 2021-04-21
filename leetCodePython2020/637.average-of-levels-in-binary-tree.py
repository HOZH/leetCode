#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        if not root:
            return []

        self.avgs = []

        queue = deque([root])

        while(len(queue)):

            current_queue_len = len(queue)
            current_length = current_queue_len
            temp_sum = 0
            while current_queue_len:

                current = queue.pop()
                if current.left:
                    queue.appendleft(current.left)
                if current.right:
                    queue.appendleft(current.right)

                temp_sum += current.val

                current_queue_len -= 1

            self.avgs.append(temp_sum/current_length)

        return self.avgs


# @lc code=end
