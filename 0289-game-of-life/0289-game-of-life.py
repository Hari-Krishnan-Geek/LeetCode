class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                tmp = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                count = 0
                for x, y in tmp:
                    x += i
                    y += j
                    if (x>=0) and (x<n) and (y>=0) and (y<m) and abs(board[x][y]) == 1:
                        count += 1
                if board[i][j] and ((count != 2) and (count != 3)):
                    board[i][j] = -1
                if (not board[i][j]) and (count == 3):
                    board[i][j] = 2
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1            
        return board                 

