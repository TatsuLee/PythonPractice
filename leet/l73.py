class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix == []:
            return None
        m, n, stack = len(matrix), len(matrix[0]), [[], []]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                        stack[0] += [i]
                        stack[1] += [j]
        for i in set(stack[0]):
            matrix[i] = [0 for k in range(n)]
        for j in set(stack[1]):
            for k in range(m):
                matrix[k][j] = 0
