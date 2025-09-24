# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p,q,r=head,None,None 
        while p!=None:
            r=q 
            q=p 
            p=p.next 
            q.next=r
        return q    
        