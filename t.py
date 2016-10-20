#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l43

a,b='123','233'
print 'input:',[a,b]
print 'true ans:', int(a)*int(b)
test = l43.Solution()
out = test.multiply(a,b)
print 'output:',out

