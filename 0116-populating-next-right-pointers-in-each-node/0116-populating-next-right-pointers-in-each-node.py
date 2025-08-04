"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        # 현재 레벨에서 가장 왼쪽 노드를 가리키는 포인터 초기화 (처음에는 루트)
        left_most = root
        # 가장 왼쪽 노드에 왼쪽 자식이 존재할 때까지 반복 (완전 이진 트리이므로 자식 중 하나만 검사)
        while left_most.left:
            # 현재 레벨을 탐색하기 위해 가장 왼쪽 노드로부터 시작하는 포인터 설정
            curr = left_most
            # 같은 레벨에서 다음 노드로 이동하면서 연결 작업 수행
            while curr:
                # 현재 노드의 왼쪽 자식의 next 포인터를 현재 노드의 오른쪽 자식으로 연결
                curr.left.next = curr.right
                # 만약 현재 노드의 next 포인터가 존재하면 (같은 레벨 오른쪽 노드가 있으면)
                if curr.next:
                    # 현재 노드의 오른쪽 자식의 next 포인터를 현재 노드 next의 왼쪽 자식으로 연결
                    curr.right.next = curr.next.left
                # 같은 레벨에서 오른쪽으로 다음 노드로 이동
                curr = curr.next
            # 다음 레벨로 이동하기 위해 가장 왼쪽 노드를 다음 레벨의 가장 왼쪽 노드로 변경
            left_most = left_most.left
        return root