#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is test template for linked list data structure


import singleLink
import l24

# init linked list
inputList = [1, 3, 5]
head = singleLink.Node(inputList[0], None)
current = head
for i in inputList[1:]:
    node = singleLink.Node(i, None)
    current.next = node
    current = current.next
print 'input'
head.show()

# run the code
test = l24.Solution()
output = test.swapPairs(head)
print 'output'
output.show()
