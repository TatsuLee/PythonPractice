#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if sum(nums[:3]) > target: return sum(nums[:3])
        if sum(nums[-3:]) < target: return sum(nums[-3:])
        ijk = []
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                while nums[j] == nums[j+1] and j < k - 1: j += 1
                while nums[k] == nums[k-1] and j < k - 1: k -= 1
                ijk.append(nums[i] + nums[j] + nums[k])
                if ijk[-1] == target: return target
                if nums[i] + nums[k-1] + nums[k] < target:
                    ijk.append(nums[i] + nums[k-1] + nums[k])
                    break
                if sum(nums[i:i+3]) > target:
                    ijk.append(sum(nums[i:i+3]))
                    break
                if len(ijk) > 1 and ijk[-1]*ijk[-2] < 0:
                    if abs(ijk[-2] - target) < abs(ijk[-1] - target): ijk.pop() 
                    continue
                if ijk[-1] < target: j += 1
                if ijk[-1] > target: k -= 1
        return ijk[-1] 
