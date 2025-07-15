class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 만약 마지막 인덱스를 제외한 곳에 0이 포함되어 있다면,
        # 특정 위치에서 멈춰서 이동이 불가능할 수 있으므로 추가 확인 필요
        if 0 in nums[:-1]:
            # 현재까지 도달할 수 있는 가장 먼 인덱스를 저장
            max_reach = 0
            # 배열을 처음부터 순회하면서 도달 가능한 범위를 점검
            for i in range(len(nums)):
                # 현재 인덱스 i가 max_reach를 넘어간다면 도달 불가능하다는 뜻 => False
                if i > max_reach:
                    return False
                # 현재 위치에서 점프 가능한 범위(i + nums[i])와 기존 max_reach 중 큰 값을 갱신
                max_reach = max(max_reach, i + nums[i])
            # 반복문을 무사히 통과했다면 마지막 인덱스까지 도달 가능한 경우 => True
            return True
        else:
            # 배열 중간에 0이 없다면 항상 도달할 수 있음 => True
            return True