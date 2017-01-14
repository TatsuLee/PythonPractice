#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        if l1.val < l2.val:
            head = l1
            ins = l2
        else:
            head = l2
            ins = l1
        prev = head
        if prev.next is None:
            prev.next = ins
            return head
        current = prev.next
        while ins:
            if ins.val < current.val:
                prev.next = ins
                prev = ins
                ins = ins.next
                prev.next = current
            else:
                if current.next is None:
                    current.next = ins
                    return head
                prev = prev.next
                current = current.next
        return head
