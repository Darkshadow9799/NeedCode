class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sub_mat = [[False] * 9 for _ in range(9)]

        for row_idx in range(9):
            for col_idx in range(9):
                unit_val = board[row_idx][col_idx]
                if unit_val == ".": continue
                unit_val = int(unit_val) - 1
                box_idx = (row_idx // 3) * 3 + (col_idx // 3)
                if (row[row_idx][unit_val] or col[col_idx][unit_val] or sub_mat[box_idx][unit_val]):
                    return False
                row[row_idx][unit_val] = True
                col[col_idx][unit_val] = True
                sub_mat[box_idx][unit_val] = True
        
        return True