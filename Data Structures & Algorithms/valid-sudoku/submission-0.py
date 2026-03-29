class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            colSet = set()
            for col in range(cols):
                if board[row][col] == ".": 
                    continue
                elif board[row][col] not in colSet:
                    colSet.add(board[row][col])
                    continue
                return False

        for col in range(cols):
            rowSet = set()
            for row in range(rows):
                if board[row][col] == ".": 
                    continue
                elif board[row][col] not in rowSet:
                    rowSet.add(board[row][col])
                    continue
                return False
        
        squareSet= set()
        for row in range(rows):
            for col in range(cols):
                val = board[row][col]
                if val == ".": 
                    continue
                boardIndex = (row//3)*3 + (col//3)
                if (boardIndex,val) in squareSet:
                    return False
                squareSet.add((boardIndex,val))
        return True
        

