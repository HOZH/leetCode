#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # 创建虚拟头节点，方便删除操作
        fast, slow = dummy, dummy

        # 让 fast 先移动 n+1 步，这样 slow 到达待删除节点的前一个节点
        for _ in range(n + 1):
            fast = fast.next

        # 让 fast 和 slow 一起移动，直到 fast 到达链表末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除目标节点
        slow.next = slow.next.next

        return dummy.next  # 返回新的头节点
        
# @lc code=end

