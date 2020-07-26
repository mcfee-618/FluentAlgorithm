class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> ListNode:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = head.next
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        head2 = self.reverseList(p1.next)
        p1.next = None
        head1 = head
        p = head = ListNode(0)
        p1 = head1
        p2 = head2
        num = 0
        while p1 is not None and p2 is not None:
            if num % 2 == 0:
                p.next = p1
                p = p1
                p1 = p1.next
            else:
                p.next = p2
                p = p2
                p2 = p2.next
            num += 1
        if p1 is not None:
            p.next = p1
        if p2 is not None:
            p.next = p2
        return head.next

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p1 = head
        p2 = None
        while p1 is not None:
            tmp = p1.next
            p1.next = p2
            p2 = p1
            p1 = tmp
        return p2

nums=[1,2,3,4,5]
p = head =ListNode(1)
for num in nums:
    tmp = ListNode(num)
    tmp.next =None
    p.next = tmp
    p=p.next

head = head.next
head = Solution().reorderList(head)
print(nums)