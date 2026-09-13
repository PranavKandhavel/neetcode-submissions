class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False

        for j in range(len(board[0])):
            seen = set()
            for i in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in seen:
                    seen.add(board[i][j])
                else:
                    return False
        for row in range(9):
            for col in range(9):

                start_row = (row // 3) * 3
                start_col = (col // 3) * 3
                seen = set()
                for i in range(start_row,start_row + 3):
                    for j in range(start_col,start_col + 3):
                        if board[i][j] == '.':
                            continue
                        if board[i][j] not in seen:
                            seen.add(board[i][j])
                        else:
                            return False
        return True