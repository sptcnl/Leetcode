class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:   # intervals가 비어있으면 빈 리스트 반환
            return []
        intervals.sort(key=lambda x: x[0])  # 각 구간의 시작점을 기준으로 정렬
        merged = [intervals[0]] # 병합된 구간을 저장할 리스트, 첫 구간을 먼저 추가
        for current in intervals[1:]:   # 두 번째 구간부터 순회
            if merged[-1][1] >= current[0]:  # 직전 구간의 끝과 현재 구간의 시작이 겹치거나 맞닿으면
                merged[-1][1] = max(merged[-1][1], current[1])  # 구간을 병합 (끝값을 더 큰 값으로 갱신)
            else:  # 겹치지 않는 경우
                merged.append(current)  # 새로운 구간을 결과에 추가
        return merged   # 병합된 구간 리스트 반환