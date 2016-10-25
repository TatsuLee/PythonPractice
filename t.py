#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l166
a, b = 4, 333 
print 'input:', [a, b]
print 'true ans:', a*1.0/b
test = l166.Solution()
out = test.fractionToDecimal(a, b)
print 'output:', out
