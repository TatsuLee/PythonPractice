#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l166
n, d = 0,-333
print 'input:', [n, d]
print 'true ans:', float(n)/d
test = l166.Solution()
out = test.fractionToDecimal(n, d)
print 'output:', out
