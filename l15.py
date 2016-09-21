#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        j, k = 1, len(nums)-2
        for i in range(len(nums)-2):
            if nums[i] != nums[i-1]:
                j, k = i + 1, len(nums)-1
                while j < k:
                    ijk = [nums[i], nums[j], nums[k]]
                    if sum(ijk) == 0 and ijk not in res:
                        res.append(ijk)
                        j += 1; k -= 1
                        continue
                    if sum(ijk) < 0:
                            j += 1
                    else:
                            k -= 1
        return res



