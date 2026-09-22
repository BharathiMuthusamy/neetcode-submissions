class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterating row
        for r in range(len(board)):
            seen_row = set()
            for c in range(len(board[0])):
                current = board[r][c]
                if current == ".":
                    continue
                if current in seen_row:
                    return False
                seen_row.add(current)
        
        #iterating column 
        for c in range(len(board[0])):
            seen_column = set()
            for r in range(len(board)):
                current = board[r][c]
                if current ==".":
                    continue
                if current in seen_column:
                    return False
                seen_column.add(current)
        
        #iterating box(3*3)
        for Row in range (0,9,3):
            for Column in range(0,9,3):
                seen_board = set()

                for r in range(Row, Row + 3):
                    for c in range(Column, Column + 3):
                        current = board[r][c]
                        if current ==".":
                            continue
                        if current in seen_board:
                            return False
                        seen_board.add(current)
        return True

