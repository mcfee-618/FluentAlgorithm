# 对链表进行插入排序
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        new_head = ListNode(1)
        new_head.next = head
        p = head.next
        last = head
        while p is not None:
            tmp = p.next
            p1 = new_head.next #指向大于的
            p2 = new_head #指向小于的
            while p!= p1:
                if p1.val>=p.val:
                    break
                p2=p1
                p1=p1.next
            if p == p1:
                last = p
                p=tmp
                continue
            p.next = p1
            p2.next = p
            last.next = tmp
            p =tmp
        return new_head.next