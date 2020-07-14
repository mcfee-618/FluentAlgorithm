# 向右旋转
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        p = head
        length = 1
        while p.next is not None:
            length += 1
            p = p.next
        k = k % length
        if k == 0:
            return head
        p.next = head
        index = 1
        p = head
        while index != length - k:
            p = p.next
            index = index + 1
        q = p.next
        p.next = None
        return q