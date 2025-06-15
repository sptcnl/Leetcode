class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [1] * (i+1)
            if i > 1:
                for j in range(1, i):
                    print(i-1, j-1, i-1, j)
                    row[j] = result[i-1][j-1] + result[i-1][j]
            print(i, row)
            result.append(row)
        return result
