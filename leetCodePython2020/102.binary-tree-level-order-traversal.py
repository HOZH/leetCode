#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.ans = []
        bag = [root]

        while len(bag) > 0:
            temp_bag = bag[:]
            bag = []
            for i in temp_bag:
                if i.left:
                    bag.append(i.left)
                if i.right:
                    bag.append(i.right)

            self.ans.append(list(map(lambda x: x.val, temp_bag)))
        return self.ans

        # self.ans = []

        # def helper(node, arr, layer):

        #     if node is None:
        #         return

        #     if len(arr) < layer+1:
        #         arr.append([])

        #     arr[layer].append(node.val)

        #     helper(node.left, arr, layer+1)
        #     helper(node.right, arr, layer+1)

        # helper(root, self.ans, 0)

        # return self.ans


# @lc code=end
