#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#

# @lc code=start
class MyLinkedList:

    class Node:
        def __init__(self, val=0, next_node=None):
            self.val = val
            self.next = next_node

    def __init__(self):
        self.placeholder_head = self.Node()

    def get(self, index: int) -> int:
        current = self.placeholder_head.next
        for _ in range(index):
            current = current.next
            if not current:
                return -1
        if current:
            return current.val
        return -1

    def addAtHead(self, val: int) -> None:
        current_head = self.placeholder_head.next
        if not current_head:
            new_head = self.Node(val, None)
            self.placeholder_head.next = new_head
        else:
            self.placeholder_head.next = self.Node(val, current_head)
        self.print_list()

    def addAtTail(self, val: int) -> None:
        current = self.placeholder_head
        while current.next:
            current = current.next
        current.next = self.Node(val, None)
        self.print_list()

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.placeholder_head
        # for _ in range(index-1):
        for _ in range(index):
            current = current.next
            if not current:
                return

        current_next = current.next
        current.next = self.Node(val, current_next)
        self.print_list()

    def deleteAtIndex(self, index: int) -> None:
        current = self.placeholder_head
        # for _ in range(index-1):
        for _ in range(index):
            current = current.next
            if not current:
                return
        current_next = current.next
        if not current_next:
            return
        else:
            current.next = current_next.next
        self.print_list()

    def print_list(self):
        return
        current = self.placeholder_head.next
        ans = []
        while current:
            ans.append(current.val)
            current = current.next
        # print(ans)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
