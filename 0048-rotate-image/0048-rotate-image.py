class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_matrix = len(matrix)
        for i in range(len_matrix):
            for j in range(i, len_matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()