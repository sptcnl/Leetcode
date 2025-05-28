# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # 0부터 시작이니 +1 반복해서 n만큼 전진
        for _ in range(n + 1):
            first = first.next
        
        # first가 맨끝으로 갈때까지 반복
        while first:
            # first와 second 전진
            first = first.next
            second = second.next
        # 다 옮겨졌으면 n번째 노드 없애기
        second.next = second.next.next
        return dummy.next