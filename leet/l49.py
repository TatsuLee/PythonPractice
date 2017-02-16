class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs <= 1:
            return strs
        strs.sort(key=lambda s: len(s))
        res, sdict = [[strs[0]]], {}
        sdict[''.join(sorted(strs[0]))] = 0
        for i in range(1, len(strs)):
            if len(strs[i]) != len(strs[i-1]):
                sdict[''.join(sorted(strs[i]))] = len(res)
                res += [[strs[i]]]
            else:
                try:
                    res[sdict[''.join(sorted(strs[i]))]] += [strs[i]]
                except:
                    sdict[''.join(sorted(strs[i]))] = len(res)
                    res += [[strs[i]]]
        return res
