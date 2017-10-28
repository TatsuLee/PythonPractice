class Solution(object):

    """
    # 1: dfs method, time complex exceeded
    def combine(self, n, k):
        def dfs(start, valuelist):
            if self.count == k:
                res.append(valuelist)
                return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        res, self.count = [], 0
        dfs(1, [])
        return res
    """
    # 2: borrowed from itertools.combinations
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return [i for i in self.combGen(range(1, n+1), k)]

    def combGen(self, iterable, r):
        # combinations('ABCD', 2) --> AB AC AD BC BD CD
        # combinations(range(4), 3) --> 012 013 023 123
        pool = list(iterable)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield list(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield list(pool[i] for i in indices)
