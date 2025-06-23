# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = "", ""

        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        num1, num2 = int(s1[::-1]), int(s2[::-1])
        total = num1 + num2
        rev_total = str(total)[::-1]

        dumy = ListNode(0)
        cur = dumy
        for i in rev_total:
            cur.next = ListNode(int(i))
            cur = cur.next
        return dumy.next