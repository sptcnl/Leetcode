# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])   # 큐에 루트 노드부터 넣어 BFS 준비
        left_to_right = True    # 왼쪽에서 오른쪽으로 탐색할지 여부 체크

        # 큐가 비어있을 때까지 반복
        while q:
            level_size = len(q)
            level_nodes = []

            # 현재 레벨의 모든 노드 탐색
            for _ in range(level_size):
                node = q.popleft()
                level_nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            # 현재 방향이 오른쪽에서 왼쪽이면 노드 값 순서를 뒤집음 (지그재그 효과)
            if not left_to_right:
                level_nodes.reverse()
            
            # 이번 레벨 결과를 최종 리스트에 추가
            result.append(level_nodes)
            # 다음 레벨은 반대 방향으로 탐색하도록
            left_to_right = not left_to_right

        return result