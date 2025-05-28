# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        
        def dfs(node, level):
            if not node:
                return
            # 현재 level에 해당하는 리스트가 없으면 추가
            if len(result) == level:
                result.append([])
            # 현재 노드의 값을 해당 level 리스트에 추가
            result[level].append(node.val)
            # 왼쪽, 오른쪽 자식 노드로 재귀 호출
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result