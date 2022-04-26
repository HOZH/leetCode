#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # patterns_to_leaves = dict()
        # nodes_level = dict()
        # nodes_by_val = dict()

        # def helper(node, pattern):
        #     if not node:
        #         return
        #     nodes_level[node.val] = len(pattern)+1
        #     nodes_by_val[node.val] = node
        #     current_pattern = pattern+(node.val,)
        #     if not node.left and not node.right:
        #         patterns_to_leaves[node.val] = current_pattern

        #     helper(node.left, current_pattern)
        #     helper(node.right, current_pattern)

        # helper(root, tuple())

        # deepst_level = max(nodes_level.values())
        # placeholder = []

        # for value in patterns_to_leaves.values():
        #     if len(value) == deepst_level:
        #         placeholder.append(value)

        # temp = set(placeholder[0])
        # for i in range(1, len(placeholder)):
        #     temp &= set(placeholder[i])

        # return nodes_by_val[max(temp, key=lambda x: nodes_level[x])]
        def post_order(node):
            if not node:
                return 0, None
            d1, n1 = post_order(node.left)
            d2, n2 = post_order(node.right)
            if d1 == d2:
                return d1+1, node
            elif d1 > d2:
                return d1+1, n1
            else:
                return d2+1, n2
        _, n = post_order(root)
        return n


# @lc code=end
