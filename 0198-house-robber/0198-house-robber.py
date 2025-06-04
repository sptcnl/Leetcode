class Solution:
    def rob(self, nums: List[int]) -> int:
        # 예외 처리: 빈 리스트 또는 단일 요소
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # 초기값 설정 (이전 집, 현재 최대값)
        prev = nums[0]
        curr = max(nums[0], nums[1])
        
        # 메인 로직: 3번째 집부터 순회
        for i in range(2, len(nums)):
            new_max = max(
                curr,          # 현재 집을 털지 않는 경우
                prev + nums[i] # 현재 집을 털고 두 칸 전까지의 최대값 사용
            )
            prev, curr = curr, new_max  # 포인터 이동
        
        return curr