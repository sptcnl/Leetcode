class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m행 n열 크기의 2차원 DP 테이블 생성, 모든 값을 1로 초기화
        # 첫 행과 첫 열은 도달할 수 있는 경로가 항상 1개이므로 1로 설정
        dp = [[1]*n for _ in range(m)]
        # 두 번째 행과 열부터 순차적으로 순회
        for i in range(1, m):
            for j in range(1, n):
                # 현재 위치 (i, j)에 도달하는 경로 수는
                # 위쪽 칸 (i-1, j)와 왼쪽 칸 (i, j-1)의 경로 수를 더한 것
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 오른쪽 아래 구석 (m-1, n-1)에서의 경로 수를 반환
        return dp[m-1][n-1]