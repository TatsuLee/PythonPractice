#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        m = 1
        current = head
        while current.next:
            m += 1
            current = current.next
        if m == n:
            return head.next
        target = head
        i = 1
        while i < m-n:
            target = target.next
            i += 1
        target.next = target.next.next
        return head
