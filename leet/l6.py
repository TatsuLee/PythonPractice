class Solution(object):

    def convert(self, s, n):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        m = len(s)
        if m <= 2 or n == 1:
            return s
        zigzag = {}
        string = ''
        h = 2*n-2
        step = (m+h-1)//h
        for i in range(step):
            for j in range(h):
                zag = i*h + j
                if zag == m:
                    break
                if j < n:
                    zigzag[j, i*(n-1)] = s[j+i*h]
                else:
                    zigzag[h-j, i*(n-1)+j+1-n] = s[zag]
        key = sorted(zigzag.keys(), key=lambda x: (x[0], x[1]))
        for k in range(m):
            string+= zigzag[key[k]]
        return string 

