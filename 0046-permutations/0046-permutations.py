class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 백트래킹 함수: 현재까지 만든 순열 path, 각 원소 사용 여부 used
        def backtrack(path, used):
            # 현재 path 길이가 nums 전체 길이와 같으면 하나의 순열 완성
            if len(path) == len(nums):
                result.append(path[:])  # 완성된 순열의 복사본을 결과에 추가
                return  # 해당 경로 종료

            # 아직 사용하지 않은 숫자를 하나씩 선택
            for i in range(len(nums)):
                if used[i]:  # 이미 사용된 숫자는 건너뛰기
                    continue
                used[i] = True           # 현재 숫자를 사용했다고 표시
                path.append(nums[i])     # 순열 경로에 현재 숫자 추가
                backtrack(path, used)    # 재귀 호출로 다음 위치 숫자 선택
                path.pop()               # 백트래킹: 마지막 숫자 제거
                used[i] = False          # 사용 해제하여 다른 순열에서 재사용 가능

        backtrack([], [False] * len(nums))  # 초기에는 빈 path와 모든 숫자 미사용
        return result
