class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 작업별 빈도수를 센다
        task_counts = Counter(tasks)
        
        # 최대 힙 만들기
        max_heap = [-cnt for cnt in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        # 쿨다운 간격을 채우면서 반복
        while max_heap:
            temp = []
            cycle = n + 1  # 한 사이클 동안 처리할 수 있는 최대 작업 수
            
            for _ in range(cycle):
                if max_heap:
                    cnt = heapq.heappop(max_heap)
                    # 작업 한 번 실행했으니 남은 횟수 1감소
                    if cnt + 1 < 0:
                        temp.append(cnt + 1)
                    time += 1
                else:
                    # 처리할 작업 없으면 idle 시간만큼 증가
                    if temp:
                        time += 1
                    else:
                        # 더이상 대기할 작업이 없으면 break
                        break
            
            # 갱신된 작업들을 다시 힙에 넣는다
            for item in temp:
                heapq.heappush(max_heap, item)
            
            # 마지막 사이클에서는 모든 작업을 완료했을 수 있으므로, break 하지 않도록 한다
        
        return time