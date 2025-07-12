class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])  # 시작점 기준 정렬
        merged = [intervals[0]]
        for current in intervals[1:]:
            if merged[-1][1] >= current[0]:  # 겹치는 경우
                merged[-1][1] = max(merged[-1][1], current[1])
            else:  # 겹치지 않는 경우
                merged.append(current)
        return merged