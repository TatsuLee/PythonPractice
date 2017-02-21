#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is test template for linked list data structure


import singleLink
import l61

# init linked list
inputList, k = [1,2,3,4,5],11 
head = singleLink.Node(inputList[0], None)
current = head
for i in inputList[1:]:
    node = singleLink.Node(i, None)
    current.next = node
    current = current.next
print 'input'
head.show()

# run the code
test = l61.Solution()
output = test.rotateRight(head, k)
print 'output'
output.show()
