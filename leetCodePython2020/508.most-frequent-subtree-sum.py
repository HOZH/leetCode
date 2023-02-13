#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import Counter


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:

        if root is None:
            return None

        self.bag = []

        def helper(node):
            if node is None:
                return 0
            left_sub_sum = helper(node.left)
            right_sub_sum = helper(node.right)

            local_sum = node.val + left_sub_sum + right_sub_sum

            self.bag.append(local_sum)

            return local_sum

        helper(root)
        temp = Counter(self.bag)
        max_count = temp.most_common(1)[0][1]

        return [i for (i, _) in filter(lambda x:x[1] == max_count, temp.items())]

        def assign_val_helper(node):
            # could just use Counter directly instead of write up this whole function

            if node is None:
                return None

            left = assign_val_helper(node.left)
            right = assign_val_helper(node.right)

            node.sum = node.val + (left.sum if left else 0) + \
                (right.sum if right else 0)
            return node

        assign_val_helper(root)

        temp = Counter()

        def traversal_helper(node, records):

            if node is None:
                return

            traversal_helper(node.left, records)

            records[node.sum] += 1

            traversal_helper(node.right, records)

        traversal_helper(root, temp)

        max_count = temp.most_common(1)[0][1]

        return [i for (i, j) in filter(lambda x:x[1] == max_count, temp.items())]


# @lc code=end
