## 链表相关

* 反转链表：
    1. 确定头和尾部，头是最后一个非空节点，尾部是头节点
    2. 双指针法，p1和p2，其中p2是p1的下一个节点
    ```
        p2=head
        p1=None
        while p2!=None:
              tmp = p2.next
              p2.next=p1
              p1=p2
              p2=tmp
        return p1      
    ```
    
* 向右旋转链表：
    1. 确定链表头和尾，链表在一个位置断开，一个为头一个为尾部
    2. 旋转长度为链表长度等于没有变化【需要求链表长度】 
    3. 头为n-k+1这个节点尾部是n-k，计数从1开始，先找新的尾节点
    4. 原来的尾节点指向head，新的尾节点指向None
     ```
         if head is None:
            return head
        p=head
        length=1
        while p.next is not None:
            length+=1
            p=p.next
        # 得到尾节点    
        k = k % length
        if k == 0:
            return head
        p.next=head
        index = 1
        p = head
        while index != length - k:
            p = p.next
            index=index+1
        #保存头结点    
        q=p.next
        p.next=None
        return q 
     ```  
 * 奇偶链表：两个头指针，两个尾指针【四指针】
 * 分隔链表：双指针法
 * 判断是否有环：定义一个快指针和慢指针,每次快指针走2步，慢指针走1步，判断快指针是否与慢指针重逢。
 * 环形链表 II返回链表开始入环的第一个节点：利用块慢指针找到相交的位置，然后利用head和fast找到共同点即可。
   
    