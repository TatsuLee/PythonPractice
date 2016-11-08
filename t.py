#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l172
import math
n = 10 
print 'input:', n
print 'true ans:', math.factorial(n)
test = l172.Solution()
out = test.trailingZeroes(n)
print 'output:', out
