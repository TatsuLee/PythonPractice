#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, val, next):
        self.val = val
        self.next = next


class SingleList(object):

    head = None
    tail = None

    def show(self):
        print "Showing list val:"
        current_node = self.head
        while current_node is not None:
            print current_node.val, "->",
            current_node = current_node.next
        print None

    def append(self, val):
        node = Node(val, None)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.val == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next


