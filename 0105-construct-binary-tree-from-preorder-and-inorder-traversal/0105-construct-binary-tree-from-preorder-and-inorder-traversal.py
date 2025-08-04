# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # preorder의 첫 번째 원소는 루트 노드 값
        root_val = preorder[0]
        # 루트 노드 생성
        root = TreeNode(root_val)
        # inorder에서 루트 노드의 인덱스를 찾아서 좌우 서브트리 구분
        root_idx = inorder.index(root_val)
        # preorder는 root 다음부터 왼쪽 서브트리 노드 수만큼 자르고 
        # inorder도 왼쪽 서브트리만 잘라 재귀 호출해 왼쪽 서브트리 생성
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        # 오른쪽 서브트리도 같은 방식으로 자르고 재귀 호출해 오른쪽 서브트리 생성
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])

        return root