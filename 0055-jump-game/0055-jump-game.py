class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach: 현재까지 도달할 수 있는 가장 먼 인덱스
        max_reach = 0
        
        # 인덱스(i)와 해당 칸에서 점프할 수 있는 최대 거리(jump)를 순회
        for i, jump in enumerate(nums):
            # 현재 위치(i)가 지금까지 도달 가능한 최대 거리(max_reach)를 넘어서면 더 이상 진행 불가
            if i > max_reach:
                return False
            
            # 현재 위치에서 점프 가능한 거리(i + jump)와 기존 최대 도달 거리 중 더 큰 값으로 갱신
            max_reach = max(max_reach, i + jump)
            
            # 최대 도달 거리가 마지막 인덱스 이상이면 True 반환 (도착 가능)
            if max_reach >= len(nums) - 1:
                return True
        
        # 모든 반복을 끝냈는데도 도달 불가능하다면 False 반환
        return False