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

    def swapPairs(self, head: ListNode) -> ListNode:
        self.swap = True
        self.prev = None

        current = head

        if head is None:
            return None

        if head.next:
            head = head.next

        while current.next is not None:
            if self.swap == True:

                temp_next = current.next

                if self.prev != None:
                    self.prev.next = temp_next

                current.next = temp_next.next
                temp_next.next = current

                self.prev = current
            else:
                current = current.next

            self.swap = not self.swap

        return head


# @lc code=end
