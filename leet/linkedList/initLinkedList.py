#!/usr/bin/env python
# -*- coding: utf-8 -*-

import LinkedList
import l21
a = [1,3,9]
b = LinkedList.SingleList()
for i in a:
    b.append(i)
b.show()
c = [2,4,11]
d = LinkedList.SingleList()
for i in c:
    d.append(i)
d.show()

test = l21.Solution()
out = test.mergeTwoLists(b.head,d.head)
print 'results:'
while out is not None:
    print out.val, "->",
    out = out.next
print None
