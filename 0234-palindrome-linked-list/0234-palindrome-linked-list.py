# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        length_of_list = 0
        stack = []
        node = head
        node2 = head
        while node:
            stack.append(node.val)
            length_of_list += 1
            node = node.next
        itr_range = length_of_list // 2 if length_of_list % 2 == 0 else (length_of_list - 1) // 2

        for i in range(itr_range):
            if node2.val == stack.pop():
                node2 = node2.next
            else:
                return False
        return True