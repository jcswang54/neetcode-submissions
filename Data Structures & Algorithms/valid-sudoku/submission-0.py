class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows  = [set() for _ in range(9)]   # rows[i]  = digits seen in row i
        cols  = [set() for _ in range(9)]   # cols[j]  = digits seen in column j
        boxes = [set() for _ in range(9)]   # boxes[b] = digits seen in box b

        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue                     # empty cell: nothing to check

                b = (i // 3) * 3 + j // 3        # which 3x3 box (0 to 8)
                if v in rows[i] or v in cols[j] or v in boxes[b]:
                    return False                 # seen before: duplicate
                rows[i].add(v)
                cols[j].add(v)
                boxes[b].add(v)
        return True