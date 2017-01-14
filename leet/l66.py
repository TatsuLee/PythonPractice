#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
                    return digits
            else:
                digits[i] = digits[i] + 1
                return digits
