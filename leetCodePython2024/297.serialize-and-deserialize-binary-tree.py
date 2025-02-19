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

        def pre_order_encode(q, arr):
            if len(q) <= 0:
                return
            node = q.popleft()
            if node is None:
                arr.append(None)
            else:
                arr.append(node.val)

                q.append(node.left)
                q.append(node.right)

            pre_order_encode(q, arr)

        pre_order_encode(queue, result)

        if len(result) == 1:
            return '[]'

        return str(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        items = filter(lambda x: x != '', data[1:-1].split(', '))
        data = deque(map(lambda x: int(x) if x != 'None' else x, items
                         ))

        if len(data) > 0:
            root = TreeNode(data.popleft())
            # discovered
            queue = deque([root])

        else:
            return None

        while len(queue) > 0:
            # form parent node first, then left then right
            node = queue.popleft()
            left = data.popleft()
            right = data.popleft()

            if left == 'None':
                node.left = None
            else:
                node.left = TreeNode(left)
                queue.append(node.left)

            if right == 'None':
                node.right = None
            else:
                node.right = TreeNode(right)
                queue.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
