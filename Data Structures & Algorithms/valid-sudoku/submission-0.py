class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            clean_row = [x for x in board[i] if x != "."]
            if not len(clean_row) == len(set(clean_row)):
                return False
            clean_col = [board[i][j] for j in range(9) if board[i][j] != "."]
            if not len(clean_col) == len(set(clean_col)):
                return False
            subcube = [board[i//3*3 + j//3][i%3*3 + j%3] for j in range(9) if board[i//3*3 + j//3][i%3*3 + j%3] != "."]
            if not len(subcube) == len(set(subcube)):
                return False
        return True