class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:  # 행렬이 비어있으면 False 반환
            return False
        row, col = 0, len(matrix[0]) - 1    # 시작 위치를 맨 위 오른쪽으로 설정
        while row < len(matrix) and col >= 0:   # 행렬 범위를 벗어나지 않는 동안 반복
            if matrix[row][col] == target:  # 현재 값이 target과 같으면 True 반환
                return True
            elif matrix[row][col] > target: # 현재 값이 target보다 크면 왼쪽으로 이동
                col -= 1
            else:   # 현재 값이 target보다 작으면 아래로 이동
                row += 1
        return False    # target을 찾지 못한 경우 False 반환