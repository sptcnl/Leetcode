# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node):
            if node:
                node_left = node.left
                node_right = node.right
                if node_left:
                    dfs(node_left)
                result.append(node.val)
                if node_right:
                    dfs(node_right)
        dfs(root)
        return result