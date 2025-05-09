from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                num = int(num)
                boxes_idx = ((r // 3) * 3) + (c // 3)

                if rows[r][num] or cols[c][num] or boxes[boxes_idx][num]:
                    return False

                rows[r][num] += 1
                cols[c][num] += 1
                boxes[boxes_idx][num] += 1

        return True