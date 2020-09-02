#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        self.ans = 0

        # if not root:
        #     return self.ans

        def helper(node):
            if not node:
                return 0

            l = helper(node.left) if node.left else -1
            r = helper(node.right) if node.right else -1

            pl, pr = 0, 0

            if l >= 0:
                if node.left.val == node.val:
                    pl = l+1

            if r >= 0:
                if node.right.val == node.val:
                    pr = r + 1

            self.ans = max(pr+pl, self.ans)

            return max(pr, pl)

            # if not node:
            #     return 1.5, 0

            # left_val, left_count = helper(node.left)
            # right_val, right_count = helper(node.right)

            # local_len = 0

            # if left_val == node.val == right_val:
            #     local_max = left_count+1+right_count
            #     return_val, return_count = node.val, max(
            #         left_count, right_count)+1

            # elif left_val == node.val:
            #     return_val, return_count = left_val, left_count+1
            #     local_max = max(right_count, return_count)

            # elif right_val == node.val:

            #     return_val, return_count = right_val, right_count+1
            #     local_max = max(left_count, return_count)

            # else:
            #     return_val, return_count = node.val, 1
            #     local_max = max(left_count, right_count, 1)

            # self.ans = max(local_max, self.ans)

            # return return_val, return_count

        helper(root)
        # return self.ans-1
        return self.ans


# @lc code=end
