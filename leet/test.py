#!/usr/bin/env python
# -*- coding: utf-8 -*-

import l74
n = [[1,   3,  5,  7], [10, 11, 16, 20], [23, 30, 34, 50]]
#n = [[1]]
print 'input:', n
test = l74.Solution()
out = test.searchMatrix(n, 16)
print 'output:', out 
