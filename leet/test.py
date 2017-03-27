#!/usr/bin/env python
# -*- coding: utf-8 -*-

import l33
n, t =  [4, 5, 6, 8, 0, 1, 2], 6 
n, t= [1,2], 1
n, t = [3,2], 3 
print 'input:', n
test = l33.Solution()
out = test.search(n, t)
print 'output:', [out, n[out]]
