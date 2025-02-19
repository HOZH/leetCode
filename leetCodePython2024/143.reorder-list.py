#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # 1. 找到链表的中点（快慢指针）
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转链表的后半部分
        prev, curr = None, slow.next
        slow.next = None  # 断开前半部分和后半部分
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second_half = prev  # 反转后的新头结点

        # 3. 交错合并两个链表
        first_half = head
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half, second_half = temp1, temp2
        
# @lc code=end

