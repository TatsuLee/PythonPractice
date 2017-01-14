#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return i+1, j+1

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortnums = sorted(list(enumerate(nums, 1)), key=lambda k: k[1])
        for i in range(len(sortnums)):
            j = i+1
            while j < len(sortnums):
                if sortnums[i][1] + sortnums[j][1] == target:
                    return sorted((sortnums[i][0], sortnums[j][0]))
                j += 1

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, n in enumerate(nums, 1):
            if n in dic:
                return [dic[n], i]
            dic[target-n] = i
