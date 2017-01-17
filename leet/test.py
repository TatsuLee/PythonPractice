#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l26
n = [1,2,3,3,3,4,4,4]
print 'input:', n
print 'true ans:', len(set(n))
test = l26.Solution()
out = test.removeDuplicates(n)
print 'output:', out
