class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



v1 = [2, 4, 3]
v2 = [5, 6, 4]


def build_node(lis):
    length = len(lis)
    if length > 0:
        head = ListNode(lis[0])
        current = head
        lis = lis[1:]
        for i in lis:
            current.next = ListNode(i)
            current = current.next

        return head

    else:
        return None
