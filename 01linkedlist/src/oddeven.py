# 奇偶链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        head1 = p1 = head
        head2 = p2 = head.next
        p = head.next.next
        count = 1
        while p is not None:
            if count % 2 != 0:
                p1.next = p
                p1 = p
            else:
                p2.next = p
                p2 = p
            p = p.next
            count += 1
        p1.next = head2
        p2.next = None
        return head1
