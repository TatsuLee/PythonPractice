#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def dtree(self, l, r, item, res):
        if r < l:  # must start with '('
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.dtree(l - 1, r, item + '(', res)
        if r > 0:
            self.dtree(l, r - 1, item + ')', res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.dtree(n, n, '', res)
        return res
