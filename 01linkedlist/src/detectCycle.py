# 环形链表2
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        if head.next == head:
            return head
        fast = head.next.next
        slow = head.next
        flag = False
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        if not flag:
            return None
        p = head
        while p!=fast:
            p=p.next
            fast=fast.next
        return p
