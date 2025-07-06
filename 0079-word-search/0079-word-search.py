class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True  # 모든 글자를 찾음
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False  # 범위 밖
            if board[r][c] != word[idx]:
                return False  # 글자가 다름

            temp = board[r][c]
            board[r][c] = '#'  # 방문 표시

            # 상, 하, 좌, 우 네 방향 탐색
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            board[r][c] = temp  # 원상복구
            return found

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        return False