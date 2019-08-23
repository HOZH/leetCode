#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        deq = collections.deque()

        current = head

        while current:

            deq.append(current.val)
            current = current.next

        # maybe I don't have to pop, just move the pivots approaching to the middle of the deque
        while len(deq) > 1:

            if deq[0] == deq[-1]:

                deq.popleft()
                deq.pop()

            else:
                return False

        return True
