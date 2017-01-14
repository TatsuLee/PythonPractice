#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def pList(self):
        curNode = self
        while curNode is not None:
            print curNode.val,
            curNode = curNode.next
        print '\n'


def iList(List):
    head = ListNode(List[0])
    curNode = head
    for i in List[1:]:
        curNode.next = ListNode(i)
        curNode = curNode.next
    return head


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode 
        """
        inc, l1.val = divmod(l1.val+l2.val, 10)
        head = l1
        while l1.next and l2.next:
            inc, l1.next.val = divmod(l1.next.val+l2.next.val+inc, 10)
            l2 = l2.next
            l1 = l1.next
        if l2.next:
            l1.next = l2.next
        while l1.next and inc:
            inc, l1.next.val = divmod(l1.next.val+inc, 10)
            l1 = l1.next
        if inc:
            l1.next = ListNode(1)
        return head 

a = [2, 4, 3, 7]
l1 = iList(a)
l1.pList()

b = [4, 5, 6, 3, 9]
l2 = iList(b)
l2.pList()

a = Solution().addTwoNumbers(l1, l2)
a.pList()
