'''
合并链表
'''
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 虚拟头结点
    dummy = ListNode(-1)
    p = dummy
    p1 = l1
    p2 = l2

    while p1 and p2:
        # 比较 p1 和 p2 两个指针
        # 将值较小的的节点接到 p 指针
        if （）:
            p.next = p1
						p1 = p1.next
        else:
            p.next = p2
						p2 = p2.next
				p = p.next

'''
分解链表
'''
def partition(head: ListNode, x: int) -> ListNode:
    # 存放小于 x 的链表的虚拟头结点
    dummy1 = ListNode(-1)
    # 存放大于等于 x 的链表的虚拟头结点
    dummy2 = ListNode(-1)
    # p1, p2 指针负责生成结果链表
    p1, p2 = dummy1, dummy2
    # 这里是将一个链表分解成两个链表
    p = head
    while p:
        if ():
            p2.next = p
            p2 = p2.next
        else:
            p1.next = p
            p1 = p1.next
        # 断开原链表中的每个节点的 next 指针
        temp = p.next
        p.next = None
        p = temp
    return dummy1.next

'''
反转列表
'''
# 定义：输入一个单链表头节点，将该链表反转，返回新的头结点
def reverse(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    last = reverse(head.next)
    head.next.next = head
    head.next = None
    return last

successor = None # 后继节点
# 反转以 head 为起点的 n 个节点，返回新的头节点
def reverseN(head: ListNode, n: int) -> ListNode:
    global successor
    if n == 1:
        # 记录第 n + 1 个节点
        successor = head.next
        return head
    # 以 head.next 为起点，需要反转前 n - 1 个节点
    last = reverseN(head.next, n - 1)

    head.next.next = head
    # 让反转之后的 head 节点和后面的节点连起来
    head.next = successor
    return last
