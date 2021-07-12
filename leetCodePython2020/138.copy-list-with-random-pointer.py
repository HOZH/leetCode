#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        current = head

        while current:
            old_next = current.next
            current.next = Node(current.val, old_next)
            current = old_next

        current = head

        while current:
            if current.next:
                current.next.random = current.random.next if current.random else None
                current = current.next.next

        head = head.next
        current = head

        while current:

            if current.next:
                old_next = current.next
                current.next = old_next.next
                current = current.next
            else:
                break

        return head


# @lc code=end
