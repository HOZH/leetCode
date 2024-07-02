#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        return second_node

        current, previous = head, None
        ans = head.next
        while current:
            sec_node_in_current_iteration = current.next
            if not sec_node_in_current_iteration:
                break
            current.next = sec_node_in_current_iteration.next

            sec_node_in_current_iteration.next = current
            if previous is not None:
                previous.next = sec_node_in_current_iteration
            previous = current
            current = current.next
        return ans


# @lc code=end
