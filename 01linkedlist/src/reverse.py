# 反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = None
        while p1 != None:
            p3 = p1.next
            p1.next = p2
            p2 = p1
            p1 = p3
        return p2

