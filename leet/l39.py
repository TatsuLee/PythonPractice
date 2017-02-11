class Solution(object):

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        import bisect

        def findComb(c, t, l):
            """
            :type c: List[int] the candidates
            :type t: int target
            :rtype l: List[List[int]]
            """
            if len(c) == 1:
                if t % c[0] == 0:
                    res.append(l+[c[0]]*(t/c[0]))
                return None
            for i in range(len(c)):
                j = 1
                while c[i]*j < t:
                    findComb(c[i+1:], t-c[i]*j, l+[c[i]]*j)
                    j += 1
                if c[i]*j == t:
                    res.append(l+[c[i]]*j)
        candidates.sort()
        res = []
        if target < candidates[0] or candidates == []:
            return res
        if target <= candidates[-1]:
            k = bisect.bisect_left(candidates, target)
            findComb(candidates[:k], target, [])
            if candidates[k] == target:
                res.append([target])
        else:
            findComb(candidates, target, [])
        return res
