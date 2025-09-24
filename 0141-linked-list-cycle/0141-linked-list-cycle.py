# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return False
        i=head
        j=head.next
        while True:
            if i==j:
                return True 
            else:
                if i.next and j.next.next:
                    i=i.next
                    j=j.next.next 
                else:
                    return False            


        