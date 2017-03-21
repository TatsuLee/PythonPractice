class Solution:

    def nthFib(self, n):  # big O(2^n)
        if n < 2:
            return n
        else:
            return self.nthFib(n-2) + self.nthFib(n-1)

    def fibSeries(self, n):
        res = [0, 1]
        for i in range(n-1):
            res.append(res[-1] + res[-2])
        return res

    def dpnthFib(self, n):  # big O(n)
        dic = {0: 0, 1: 1}
        if n < 2:
            return n
        if n in dic:
            return dic[n]
        else:
            dic[n] = self.dpnthFib(n-1) + self.dpnthFib(n-2)
            return dic[n]
