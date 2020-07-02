#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        result = []
        queue = deque([root])

        def helper(q, arr):

            if len(q) <= 0:
                return
            node = q.popleft()
            if node is None:
                arr.append(None)
            else:
                arr.append(node.val)

                q.append(node.left)
                q.append(node.right)

            helper(q, arr)

        helper(queue, result)

        if len(result) == 1:
            return '[]'

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = deque(map(lambda x: int(x) if x != 'None' else x,
                         filter(lambda x: x != '', data[1:-1].split(', '))))

        temp = None

        if len(data) > 0:

            # discovered
            temp = TreeNode(data.popleft())

            queue = deque([temp])

        else:
            return None

        def helper(discovered, dataset):
            if len(discovered) <= 0:
                return
            node = discovered.popleft()
            left = dataset.popleft()
            right = dataset.popleft()

            if left == 'None':
                node.left = None
            else:
                node.left = TreeNode(left)
                discovered.append(node.left)

            if right == 'None':
                node.right = None
            else:
                node.right = TreeNode(right)
                discovered.append(node.right)

            helper(discovered, dataset)

        helper(queue, data)
        return temp


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
