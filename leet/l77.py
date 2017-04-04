class Solution(object):

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
