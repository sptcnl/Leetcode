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
        
        # first를 n+1칸 앞으로 이동
        for _ in range(n + 1):
            first = first.next
        
        # first가 끝에 도달할 때까지 두 포인터 같이 이동
        while first:
            first = first.next
            second = second.next
        
        # second.next가 삭제할 노드
        second.next = second.next.next
        
        return dummy.next