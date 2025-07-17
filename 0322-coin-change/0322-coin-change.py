class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]를 i 금액을 만들기 위한 최소 동전 개수로 정의하고 무한대로 초기화
        dp = [float('inf')] * (amount + 1)
        # 0 금액을 만들기 위해 필요한 동전 개수는 0개
        dp[0] = 0
        # 각 동전을 기준으로 반복
        for coin in coins:
            # coin부터 amount까지 모든 금액에 대해 최소 동전 개수 갱신
            for i in range(coin, amount + 1):
                # 현재 금액 i를 만들기 위한 최소 동전 개수 
                # vs. (i - coin) 금액을 만들기 위한 동전 수 + 지금 coin 1개 추가한 값 중 최소값 선택
                dp[i] = min(dp[i], dp[i - coin] + 1)
        # amount 금액을 만들 수 없으면 -1 반환, 아니면 최소 동전 개수 반환
        return -1 if dp[amount] == float('inf') else dp[amount]