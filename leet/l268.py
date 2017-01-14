#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 1:
                return abs(nums[0] - 1)
        else:
            return self.da(nums)

    def da(self, nums):
        n = len(nums)
        mid = (nums[0] + nums[-1])/2.0
        if n % 2 == 0:  # list is even
            if nums[n/2-1] == mid:  # go with left
                return self.da(nums[:n/2])
            elif nums[n/2] == mid:  # go with right
                return self.da(nums[n/2:])
            elif (nums[0]+nums[-1]) % 2 == 0:
                return int(mid)
            else:
                if nums[0] == 0:
                    return nums[-1]+1
                else:
                    return nums[0]-1
        if n % 2 != 0:  # list is odd
            if nums[n/2] < mid:
                return self.da(nums[n/2:])
            elif nums[n/2] > mid:
                return self.da(nums[:n/2+1])
            else:
                if nums[0] == 0:
                    return nums[-1]+1
                else:
                    return nums[0]-1

