#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def end_of_first_half(node):
            fast = node
            slow = node
            while fast.next is not None and fast.next.next is not None:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(node):
            previous = None
            current = node
            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        sec_head = end_of_first_half(head).next
        tail = reverse(sec_head)

        while tail is not None:
            if head.val == tail.val:
                head = head.next
                tail = tail.next
            else:
                return False
        return True


# @lc code=end
