#!/usr/bin/env python
# -*- coding: utf-8 -*-

import LinkedList
import l19
a = '123456'
b = LinkedList.SingleList()
for i in a:
    b.append(i)
b.show()
test = l19.Solution()
out = test.removeNthFromEnd(b.head, 2)
print b.show() 

