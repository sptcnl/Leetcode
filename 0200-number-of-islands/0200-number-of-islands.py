class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            visit(i+1, j)
            visit(i-1, j)
            visit(i, j+1)
            visit(i, j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    visit(i, j)
                    count += 1
        return count