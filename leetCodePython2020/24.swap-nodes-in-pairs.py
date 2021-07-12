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

        if not head or not head.next:
            return head

        first_nodes, sec_nodes = [], []

        index = 0

        current = head
        while current:

            if index % 2 == 0:
                sec_nodes.append(current)
            else:
                first_nodes.append(current)

            index += 1
            current = current.next

        result = first_nodes.pop(0)
        current = result

        while first_nodes or sec_nodes:
            if sec_nodes:
                current.next = sec_nodes.pop(0)
                current = current.next

            if first_nodes:
                current.next = first_nodes.pop(0)
                current = current.next

        current.next = None

        return result

    def swapPairs_temp(self, head: ListNode) -> ListNode:
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
