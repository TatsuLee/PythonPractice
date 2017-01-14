#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area = (D-B)*(C-A) + (H-F)*(G-E)
        area -= max((min(D, H)-max(B, F)), 0)*max((min(C, G)-max(A, E)), 0)
        return area
