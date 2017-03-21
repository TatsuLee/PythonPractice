#!/usr/bin/env python
# -*- coding: utf-8 -*-

import timeit
import fib
n = 10 
print 'input:', n
test = fib.Solution()
out1 = test.nthFib(n)
print 'output1:', out1 
out2 = test.fibSeries(n)
print 'output2:', out2
out3 = test.dpnthFib(n)
print 'output3:', out3
# time test
i, ntest = 20, 20
print 'time1:', timeit.timeit('fib.Solution().nthFib(ntest)', 'from __main__ import fib, ntest', number = i)
print 'time2:', timeit.timeit('fib.Solution().fibSeries(ntest)', 'from __main__ import fib, ntest', number = i)
print 'time3:', timeit.timeit('fib.Solution().dpnthFib(ntest)', 'from __main__ import fib, ntest', number = i)
