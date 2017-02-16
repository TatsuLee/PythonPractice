class Solution(object):

    def spiralOrder(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        try:
            while True:
                res += matrix.pop(0)  # get row 0
                res += [i.pop(-1) for i in matrix]  # get col -1
                res += matrix.pop(-1)[::-1]  # get row -1
                res += [i.pop(0) for i in matrix[::-1]]  # get col 0
        except:
            return res
