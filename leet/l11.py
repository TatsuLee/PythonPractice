#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        if r <= 0:
            return 0
        area = 0
        while l < r:
            area = max(min(height[l], height[r])*abs(l-r), area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area
