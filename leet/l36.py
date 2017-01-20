class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # generate 3 empty list to store scaned nums
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        grid = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                curDigit = board[i][j]
                if curDigit == '.':
                    continue
                if curDigit in row[i]:
                    return False
                if curDigit in col[j]:
                    return False
                k = i/3*3+j/3  # find the grid num with (i,j)
                if curDigit in grid[k]:
                    return False
                grid[k].add(curDigit)
                row[i].add(curDigit)
                col[j].add(curDigit)
        return True
