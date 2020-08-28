#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        else:
            result = ListNode()
            current = result
            carry = 0
            while l1 or l2 or carry:
                new_val = (0 if not l1 else l1.val) + \
                    (0 if not l2 else l2.val)+carry

                if new_val >= 10:
                    carry = 1
                    new_val -= 10
                else:
                    carry = 0
                current.next = ListNode(new_val)
                current = current.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
        result = result.next
        return result

# @lc code=end
