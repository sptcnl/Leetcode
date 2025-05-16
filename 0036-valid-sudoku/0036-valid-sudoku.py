from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 각각 열, 행, 3x3 박스를 저장할 defaultdict
        cols = defaultdict(list)  # 열은 j 기준
        rows = defaultdict(list)  # 행은 i 기준
        boxes = defaultdict(list)  # 박스는 (i//3, j//3) 조합 기준

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                
                # 3x3 박스 인덱스 계산
                box_index = (i // 3) * 3 + (j // 3)
                
                # 중복 체크
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in boxes[box_index]):
                    return False
                
                # 값 저장
                rows[i].append(num)
                cols[j].append(num)
                boxes[box_index].append(num)
        
        return True