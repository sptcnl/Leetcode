# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        len_of_list = 0
        stack  = []
        cur = head
        while cur:
            stack.append(cur.val)
            len_of_list += 1
            cur = cur.next
        itr_range = len_of_list // 2
        cur = head
        for i in range(itr_range):
            if cur.val != stack.pop():
                return False
            cur = cur.next
        return True