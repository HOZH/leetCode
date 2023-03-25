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
        if not head:
            return None
        arr = []
        temp = []

        while head:
            arr.append(head)
            head = head.next
        temp = deque()
        liz = deque()
        len_arr = len(arr)
        for i in range(len_arr, 0, -1):
            if len_arr-i+1 != n:
                temp.appendleft(arr[i-1])
                liz.appendleft(arr[i-1].val)

        if (n == 1 and not len(temp)):
            return None

        head = ans = temp[0]

        for i in range(1, len(temp)):
            head.next = temp[i]
            head = temp[i]
        head.next = None
        return ans

# @lc code=end
