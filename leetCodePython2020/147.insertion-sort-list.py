#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # def insertionSortList_temp(self, head: ListNode) -> ListNode:

    #     if head is None or head.next is None:
    #         return head

    #     tail, current = head, head

    #     while current is not None:
    #         temp_current = head

    #         while temp_current is not tail:
    #             # print(temp_current is tail, temp_current.val, tail.val)
    #             if current.val < temp_current.val:

    #                 temp_val = temp_current.val

    #                 temp_current.val = current.val

    #                 # start pushing back vals by one position

    #                 while temp_current is not tail:

    #                     next_val = temp_current.next.val

    #                     temp_current.next.val = temp_val
    #                     temp_current = temp_current.next
    #                     temp_val = next_val

    #             else:
    #                 temp_current = temp_current.next

    #         tail = tail.next
    #         current = tail

    #     return head

    def insertionSortList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        current, global_prev = head, None
        global_tail = head

        while current is not None:
            temp_current, prev = head, None
            if current.val < head.val:
                head = ListNode(current.val, head)
                global_prev.next = current.next
                current = global_prev

            elif current.val > global_tail.val:
                pass

            else:

                while temp_current is not current:
                    if current.val < temp_current.val:
                        if prev:
                            prev.next = ListNode(current.val, temp_current)

                        else:
                            head = ListNode(current.val, head)

                        global_prev.next = current.next

                        current = global_prev
                        break

                    else:
                        prev, temp_current = temp_current, temp_current.next

            global_prev, current = current, current.next
            global_tail = global_prev

        return head

# @lc code=end
