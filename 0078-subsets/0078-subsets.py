class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # 부분집합을 생성하는 재귀 함수
        def dfs(idx, path):
            result.append(path[:])  # 현재 경로(부분집합)를 결과에 복사해서 추가
            # idx부터 시작해서 각 요소에 대해 부분집합 만들기 시도
            for i in range(idx, len(nums)):
                path.append(nums[i])    # 현재 숫자를 부분집합에 포함
                dfs(i+1, path)  # 다음 인덱스로 재귀 호출
                path.pop()  # 재귀 호출 이후, 현재 숫자를 빼주어(백트래킹) 다른 경로 탐색
        dfs(0, [])
        return result