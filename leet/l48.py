class Solution(object):

    def rotate(self, matrix):

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)-1
        if n <= 0:
            return None
        for i in range((n+1)/2):
            for j in range(i, n-i):
                matrix[i][j], matrix[j][n-i], matrix[n-i][n-j], matrix[n-j][i] \
                = matrix[n-j][i], matrix[i][j], matrix[j][n-i], matrix[n-i][n-j]
