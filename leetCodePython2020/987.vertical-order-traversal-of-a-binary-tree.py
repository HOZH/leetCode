#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        # temp_result = defaultdict(list)
        # stack = deque()

        # if root:
        #     stack.append((root, 0))

        # while len(stack):
        #     current_len = len(stack)
        #     temp_dict = defaultdict(list)
        #     while current_len:
        #         current, current_index = stack.popleft()
        #         temp_dict[current_index].append(current.val)
        #         if current.left:
        #             stack.append((current.left, current_index-1))
        #         if current.right:
        #             stack.append((current.right, current_index+1))
        #         current_len -= 1
        #     for i in temp_dict.keys():
        #         temp_result[i].extend(sorted(temp_dict[i]))

        # result = []
        # for i in sorted(temp_result.keys()):
        #     result.append(temp_result[i])

        # return result

        if not root:
            return []
        vals = []

        def preorder(x, y, node):
            if not node:
                return
            vals.append((x, y, node.val))
            preorder(x-1, y+1, node.left)
            preorder(x+1, y+1, node.right)

        preorder(0, 0, root)

        ans = []

        last_x = float('-inf')
        for x, y, val in sorted(vals):
            if x != last_x:
                ans.append([])
                last_x = x
            ans[-1].append(val)

        return ans


# @lc code=end
