# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        # 스택에 노드가 있거나 현재 노드가 None이 아닐 동안 반복
        while stack or current:
            # 현재 노드가 존재하면, 왼쪽 자식 노드를 찾아 계속 내려가기
            while current:
                stack.append(current)   # 현재 노드를 스택에 저장
                current = current.left  # 왼쪽 자식 노드로 이동
            
            # 스택에서 가장 위 노드 꺼내기 (왼쪽 끝 노드부터 방문)
            current = stack.pop()

            # 방문한 노드 수 하나 줄이기 (k번째 노드 찾기 위한 카운트다운)
            k -= 1
            # k번째 방문한 노드라면 값 반환
            if k == 0:
                return current.val
            
            # 오른쪽 자식 노드로 이동해 그 서브트리 탐색 계속
            current = current.right