class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):    # 단어의 모든 문자를 찾았다면 True 반환
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols:    # 격자를 벗어난 경우 False
                return False
            if board[r][c] != word[idx]:    # 현재 위치 문자가 단어의 해당 글자가 아니면 False
                return False
            temp = board[r][c]  # 현재 문자를 저장(복구용)
            board[r][c] = '#'   # 방문 표시(다시 방문 방지)
            # 상, 하, 좌, 우 방향으로 DFS 탐색 진행
            result = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
            )
            board[r][c] = temp  # 원래 문자로 복구(백트래킹)
            return result
        # 격자의 각 위치에서 DFS 시작
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):    # 단어의 첫 글자부터 매칭 시작
                    return True
        return False    # 모든 위치를 탐색해도 단어를 못 찾으면 False