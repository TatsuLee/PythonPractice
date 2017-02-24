#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l71
n = '/home/..//./'
n = '/a/./b/../../c/'
print 'input:', n
test = l71.Solution()
out = test.simplifyPath(n)
print 'output:', out
