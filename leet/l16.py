#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if sum(nums[:3]) > target:
            return sum(nums[:3])
        if sum(nums[-3:]) < target:
            return sum(nums[-3:])
        ijk = sum(nums[:3])
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tmpsum = nums[i] + nums[j] + nums[k]
                if tmpsum == target:
                    return target
                elif tmpsum < target:
                    j += 1
                elif tmpsum > target:
                    k -= 1
                if abs(tmpsum - target) < abs(ijk - target):
                    ijk = tmpsum
        return ijk
