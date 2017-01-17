class Solution(object):

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m, n = len(needle), len(haystack)
        if needle == '' or (m == n and haystack == needle):
            return 0
        if m > n or (m == n and haystack is not needle):
            return -1
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1
