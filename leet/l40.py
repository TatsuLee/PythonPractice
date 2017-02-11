class Solution(object):

    def combinationSum2(self, candidates, target):
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
                if t == c[0]:
                    res.append(l+[t])
                return None
            for i in range(len(c)):
                if i > 0 and c[i] == c[i-1]:
                    continue
                if c[i] < t:
                    findComb(c[i+1:], t-c[i], l+[c[i]])
                elif c[i] == t:
                    res.append(l+[t])
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
