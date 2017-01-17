#!/usr/bin/env python
# -*- coding: utf-8 -*-


import l27
n =nums = [3,2,3,3,3,4,4,4]
val = 3
print 'input:', n
n.remove(3)
print 'true ans:', n
test = l27.Solution()
out = test.removeElement(n,3)
print 'output:', n[:out] 

print 'test:'
m, n = 0, len(nums)
for i in range(n):
    if nums[i] == val:
        continue
    else:
        nums[m] = nums[i]
        print nums
        m += 1
