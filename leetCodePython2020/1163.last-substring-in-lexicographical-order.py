#
# @lc app=leetcode id=1163 lang=python3
#
# [1163] Last Substring in Lexicographical Order
#

# @lc code=start


class Node:
    def __init__(self, start, end, value=float('-inf')):
        self.start = start
        self.end = end
        self.value = value


class Solution:

    def lastSubstring(self, s: str) -> str:

        root = Node(0,len(s))


        def build_tree(node):

            if node.start!=node.end:

            else:
                node.value = 



        # @lc code=end
