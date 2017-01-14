#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # iteritive
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        newhead = None
        current = head
        while current is not None:
            nxt = current.next
            current.next = newhead
            newhead = current
            current = nxt
        return newhead



